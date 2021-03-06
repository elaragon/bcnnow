'''
    BarcelonaNow (c) Copyright 2018 by the Eurecat - Technology Centre of Catalonia

    This source code is free software; you can redistribute it and/or
    modify it under the terms of the GNU Public License as published
    by the Free Software Foundation; either version 3 of the License,
    or (at your option) any later version.

    This source code is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    Please refer to the GNU Public License for more details.

    You should have received a copy of the GNU Public License along with
    this source code; if not, write to:
    Free Software Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
'''

import json
import math

# This class defines the structure of the payload field for an instance of an Inside Airbnb Listing BaseRecord.
class OHBPayload3:

    def __init__(self):
        self.period = ''
        self.value = 0.0

    def setPeriod(self, period):
        self.period = str(period)

    def setValue(self, value):
        if math.isnan(value):
            self.value = 0.0
        else:
            self.value = value

    def getPeriod(self):
        return self.period

    def getValue(self):
        return self.value

    def toJSON(self):
        return '{"period": ' + json.dumps(self.getPeriod()) + ', "value": ' + json.dumps(self.getValue()) + '}'