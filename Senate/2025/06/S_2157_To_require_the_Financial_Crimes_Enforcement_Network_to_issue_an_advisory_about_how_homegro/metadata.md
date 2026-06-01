# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2157?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2157
- Title: Gun Violence Prevention Through Financial Intelligence Act
- Congress: 119
- Bill type: S
- Bill number: 2157
- Origin chamber: Senate
- Introduced date: 2025-06-24
- Update date: 2026-01-10T07:08:38Z
- Update date including text: 2026-01-10T07:08:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-24: Introduced in Senate
- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-24: Introduced in Senate

## Actions

- 2025-06-24 - IntroReferral: Introduced in Senate
- 2025-06-24 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-24",
    "latestAction": {
      "actionDate": "2025-06-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2157",
    "number": "2157",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Gun Violence Prevention Through Financial Intelligence Act",
    "type": "S",
    "updateDate": "2026-01-10T07:08:38Z",
    "updateDateIncludingText": "2026-01-10T07:08:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-24",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-06-24T21:08:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CT"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "NJ"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2157is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2157\nIN THE SENATE OF THE UNITED STATES\nJune 24, 2025 Mr. Markey (for himself, Mr. Blumenthal , Ms. Hirono , Mr. Booker , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Financial Crimes Enforcement Network to issue an advisory about how homegrown violent extremists and other perpetrators of domestic terrorism procure firearms and firearm accessories, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gun Violence Prevention Through Financial Intelligence Act .\n#### 2. Advisory on the procurement of firearms and firearm accessories\n##### (a) Definitions\nIn this section:\n**(1) Domestic terrorism**\nThe term domestic terrorism has the meaning given the term in section 2331 of title 18, United States Code.\n**(2) FinCEN**\nThe term FinCEN means the Financial Crimes Enforcement Network.\n**(3) Financial institution**\nThe term financial institution has the meaning given the term in section 5312(a) of title 31, United States Code.\n**(4) Firearm**\nThe term firearm has the meaning given the term in section 921(a) of title 18, United States Code.\n##### (b) Request for information\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, FinCEN shall request information from financial institutions for the purpose of developing an advisory about the identification and reporting of suspicious activity relating to\u2014\n**(A)**\nhow homegrown violent extremists and perpetrators of domestic terrorism procure firearms and firearm accessories for the purpose of carrying out lone actor or lone wolf acts of terror within the United States; and\n**(B)**\nthe ways in which the firearms market in the United States is exploited to facilitate gun violence in the United States.\n**(2) Application of section 5318(g) of title 31**\nSection 5318(g) of title 31, United States Code, shall apply to a request for information from a financial institution by FinCEN under paragraph (1) in the same manner that section applies to a requirement by the Secretary of the Treasury of a financial institution to report a suspicious transaction under that section.\n**(3) Tailoring**\nIn requesting information from a financial institution under paragraph (1), FinCEN shall consider the size of the financial institution and tailor the request accordingly.\n**(4) Consultation**\nBefore requesting information from a financial institution under paragraph (1), FinCEN shall consult, with respect to the nature of the request, with\u2014\n**(A)**\nthe Director of the Federal Bureau of Investigation;\n**(B)**\nthe Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives of the Department of Justice; and\n**(C)**\nsellers of firearms and firearm accessories.\n##### (c) Advisory\n**(1) Sufficient information collected**\nNot later than 540 days after the date of enactment of this Act, if FinCEN determines that the information collected under subsection (b)(1) is sufficient to develop the advisory described in that subsection, FinCEN shall issue the advisory.\n**(2) Insufficient information collected**\nNot later than 540 days after the date of enactment of this Act, if FinCEN determines that the information collected under subsection (b)(1) is not sufficient to develop the advisory described in that subsection, FinCEN shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that describes\u2014\n**(A)**\nthe type information collected under subsection (b)(1);\n**(B)**\nthe methodology used to collect such information;\n**(C)**\nthe degree to which financial institutions provided information requested;\n**(D)**\nwhy such information is not sufficient to develop the advisory described in subsection (b)(1); and\n**(E)**\nany barriers to obtaining the information that is required to develop the advisory described in subsection (b)(1).\n##### (d) Rulemaking\nNot later than 90 days after the date of enactment of this Act, FinCEN, in consultation with the Director of the Federal Bureau of Investigation and the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives of the Department of Justice, shall promulgate a rule that defines the following terms for the purpose of this section:\n**(1)**\nFirearm accessory.\n**(2)**\nHomegrown violent extremist.\n**(3)**\nLone wolf.\n**(4)**\nLone actor.",
      "versionDate": "2025-06-24",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-06-27",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4220",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gun Violence Prevention Through Financial Intelligence Act",
      "type": "HR"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-14T16:02:13Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2157is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Gun Violence Prevention Through Financial Intelligence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-04T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Gun Violence Prevention Through Financial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-04T02:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Financial Crimes Enforcement Network to issue an advisory about how homegrown violent extremists and other perpetrators of domestic terrorism procure firearms and firearm accessories, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-04T02:18:35Z"
    }
  ]
}
```
