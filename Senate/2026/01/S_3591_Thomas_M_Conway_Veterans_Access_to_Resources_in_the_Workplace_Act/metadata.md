# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3591
- Title: Thomas M. Conway Veterans Access to Resources in the Workplace Act
- Congress: 119
- Bill type: S
- Bill number: 3591
- Origin chamber: Senate
- Introduced date: 2026-01-07
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in Senate
- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2026-01-07: Introduced in Senate

## Actions

- 2026-01-07 - IntroReferral: Introduced in Senate
- 2026-01-07 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3591",
    "number": "3591",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000383",
        "district": "",
        "firstName": "Angus",
        "fullName": "Sen. King, Angus S., Jr. [I-ME]",
        "lastName": "King",
        "party": "I",
        "state": "ME"
      }
    ],
    "title": "Thomas M. Conway Veterans Access to Resources in the Workplace Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-07",
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
        "item": [
          {
            "date": "2026-04-29T21:37:20Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-01-07T20:36:24Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3591is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3591\nIN THE SENATE OF THE UNITED STATES\nJanuary 7, 2026 Mr. King (for himself and Mr. Banks ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Labor, in coordination with the Secretary of Veterans Affairs, to develop a notice detailing benefits available to veterans, and to require employers to display such notice, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Thomas M. Conway Veterans Access to Resources in the Workplace Act .\n#### 2. Display of veterans benefits notice\n##### (a) Display requirement\nEach employer shall post and keep posted, in conspicuous places on the premises of the employer where notices to employees and applicants for employment are customarily posted, the notice developed under subsection (b) for the State in which such premises is located.\n##### (b) Notice\n**(1) In general**\n**(A) Development; publication**\n**(i) In general**\nNot later than 270 days after the date of the enactment of this Act, the Secretary of Labor (acting through the Veterans' Employment and Training Service), in coordination with the Secretary of Veterans Affairs (in consultation with the Veterans Experience Office), shall develop and publish a notice for each State detailing benefits for veterans under the laws administered by such Secretaries.\n**(ii) Benefits under State law**\nThe Secretary of Labor shall ensure that each State is given a 45-day period to provide information on benefits for veterans under State law to be included in the notice for such State.\n**(B) Review**\n**(i) In general**\nNot less frequently than twice each year, the Secretary of Labor, in coordination with the Secretary of Veterans Affairs, shall review, and update as necessary, each notice developed under this paragraph.\n**(ii) State updates**\nIn carrying out clause (i), the Secretary of Labor shall ensure that each State is given the opportunity to update the information included in the notice for such State.\n**(2) Contents**\nEach notice developed under paragraph (1) shall at a minimum include information on the following:\n**(A)**\nThe Veterans Crisis Line.\n**(B)**\nHow to apply for the benefits described in paragraph (1)(A).\n**(C)**\nInformation on benefits for veterans under the law of the applicable State, if the State provides such information as described in paragraph (1).\n**(3) Publication; design**\nEach notice developed under paragraph (1) shall be\u2014\n**(A)**\nmade publicly available on the websites of the Department of Labor and the Department of Veterans Affairs; and\n**(B)**\ndesigned to be published on an 8.5-inch by 11-inch sheet of paper.\n##### (c) Information campaign\nDuring the 180-day period beginning on the date of the enactment of this Act, the Secretary of Labor, in coordination with the Secretary of Veterans Affairs, shall conduct an information campaign to inform employers of\u2014\n**(1)**\nthe notices developed under subsection (b); and\n**(2)**\nthe requirement to display the notice under subsection (a).\n##### (d) Definitions\nIn this Act:\n**(1) Employee; person**\nThe terms employee and person have the meanings given those terms in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ).\n**(2) Employer**\n**(A) In general**\nThe term employer \u2014\n**(i)**\nmeans any person engaged in commerce or in any industry or activity affecting commerce who employs 50 or more employees for each working day during each of 20 or more calendar workweeks in the current or preceding calendar year; and\n**(ii)**\nincludes\u2014\n**(I)**\nany person who acts, directly or indirectly, in the interest of an employer to any of the employees of such employer;\n**(II)**\nany successor in interest of an employer;\n**(III)**\nany public agency (as defined in section 3(x) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203(x) ));\n**(IV)**\nthe Government Accountability Office; and\n**(V)**\nthe Library of Congress.\n**(B) Public agency**\nFor purposes of subparagraph (A)(ii)(III), a public agency shall be considered to be a person engaged in commerce or in an industry or activity affecting commerce.\n**(3) State**\nThe term State includes each of the several States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, and the United States Virgin Islands.\n##### (e) Effective dates\n**(1) In general**\nExcept as specified in paragraph (2), the provisions of this Act shall take effect on the date of the enactment of this Act.\n**(2) Effective date for display requirement**\nSubsection (a) shall take effect on the date that is one year after the date of the enactment of this Act.",
      "versionDate": "2026-01-07",
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
        "actionDate": "2026-01-29",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "6960",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Thomas M. Conway Veterans Access to Resources in the Workplace Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-02-09T19:01:48Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3591is.xml"
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
      "title": "Thomas M. Conway Veterans Access to Resources in the Workplace Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Labor, in coordination with the Secretary of Veterans Affairs, to develop a notice detailing benefits available to veterans, and to require employers to display such notice, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:36Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Thomas M. Conway Veterans Access to Resources in the Workplace Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
