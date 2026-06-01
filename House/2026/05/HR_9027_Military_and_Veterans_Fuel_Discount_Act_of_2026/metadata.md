# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/9027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/9027
- Title: Military and Veterans Fuel Discount Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 9027
- Origin chamber: House
- Introduced date: 2026-05-26
- Update date: 2026-05-30T08:06:02Z
- Update date including text: 2026-05-30T08:06:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-26: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-05-26: Introduced in House

## Actions

- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Introduced in House
- 2026-05-26 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-26",
    "latestAction": {
      "actionDate": "2026-05-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/9027",
    "number": "9027",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Military and Veterans Fuel Discount Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:02Z",
    "updateDateIncludingText": "2026-05-30T08:06:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-26",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2026-05-26T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
      "state": "NE"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-26",
      "state": "NC"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "VA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9027ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 9027\nIN THE HOUSE OF REPRESENTATIVES\nMay 26, 2026 Mr. Hamadeh of Arizona (for himself, Mr. Panetta , Mr. Bacon , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the Secretary of Defense to carry out a program to provide to certain patrons a discount on motor fuel sold at exchange stores, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military and Veterans Fuel Discount Act of 2026 .\n#### 2. Program to provide to certain patrons a discount on motor fuel sold at exchange stores\n##### (a) In general\nThe Secretary of Defense may, if there is a tax described in subsection (b) applicable to motor fuel, carry out a program to provide to eligible patrons a discount on such motor fuel\u2014\n**(1)**\nsold at an exchange store; and\n**(2)**\ndispensed directly into a vehicle owned by an eligible patron.\n##### (b) Amount of discount\n**(1) Base discount**\nA discount provided under subsection (a) shall be an amount not less than\u2014\n**(A)**\nthe rate of tax applicable to gasoline under section 4081 of the Internal Revenue Code of 1986 ( 26 U.S.C. 4081 ), except that such discount may not be less than 18.4 cents per gallon; and\n**(B)**\nthe rate of tax applicable to diesel fuel under such section 4081, except that such discount may not be less than 24.4 cents per gallon.\n**(2) Authorization of supplemental discount**\nThe Secretary may, if there is a State or local tax applicable to such motor fuel, provide an additional discount to an eligible patron, with respect to each gallon of motor fuel sold at an exchange store, of such amount as the Secretary determines appropriate.\n##### (c) Automatic application\nThe Secretary shall, to the maximum extent practicable, ensure that a discount provided under this section is applied upon the sale of motor fuel at an exchange store to an eligible patron.\n##### (d) Regulations\nThe Secretary shall update any appropriate regulations to prevent\u2014\n**(1)**\nfraud or abuse of a program carried out under this section; and\n**(2)**\nthe resale or commercial use of motor fuel purchased at a discount under this section.\n##### (e) Termination\nThe authority of the Secretary to provide a discount under this section shall terminate on September 30, 2029.\n##### (f) Report\nNot later than 180 days after the date on which the Secretary carries out a program under this section, and annually thereafter until the termination under subsection (e), the Secretary shall submit to the Committees on Armed Services of the House of Representatives and the Senate a report on such a program, including\u2014\n**(1)**\nthe number of exchange stores, disaggregated by exchange system, that sold motor fuel subject to a discount under subsection (b)(1);\n**(2)**\nthe total gallons of such motor fuel sold annually by\u2014\n**(A)**\neach exchange store;\n**(B)**\nall exchange stores; and\n**(C)**\nall exchange stores, disaggregated by exchange system;\n**(3)**\nthe total annual cost of the discount under subsection (b)(1)(A);\n**(4)**\nthe total annual cost of any additional discount under subsection (b)(1)(B);\n**(5)**\nthe average amount of motor fuel sold annually by each exchange store before the date of the enactment of this Act;\n**(6)**\nany identified fraud, abuse, or issues with implementation with respect to such program; and\n**(7)**\nany recommendations with respect to continuing or modifying such program.\n##### (g) Coordination\nNothing in this section shall be construed to prohibit the Secretary from coordinating with the heads of other Federal departments or agencies to encourage the adoption of similar policies with respect to discounts on motor fuel\u2014\n**(1)**\nfor members of the uniformed services; or\n**(2)**\nother persons served by exchange systems outside the Department of Defense.\n##### (h) Eligible patron defined\nThe term eligible patron means a person who is authorized under Federal law and applicable regulations to purchase motor fuel from a fuel station operated by an exchange store.",
      "versionDate": "2026-05-26",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr9027ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military and Veterans Fuel Discount Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-27T08:23:29Z"
    },
    {
      "title": "Military and Veterans Fuel Discount Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-27T08:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Defense to carry out a program to provide to certain patrons a discount on motor fuel sold at exchange stores, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-27T08:18:34Z"
    }
  ]
}
```
