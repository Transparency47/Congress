# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/509?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/509
- Title: Future Logging Careers Act
- Congress: 119
- Bill type: S
- Bill number: 509
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-04-21T12:24:17Z
- Update date including text: 2025-04-21T12:24:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/509",
    "number": "509",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Future Logging Careers Act",
    "type": "S",
    "updateDate": "2025-04-21T12:24:17Z",
    "updateDateIncludingText": "2025-04-21T12:24:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T16:13:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "ID"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s509is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 509\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Risch (for himself, Mr. King , Ms. Collins , Mr. Crapo , Mr. Cornyn , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo exempt certain 16- and 17-year-old individuals employed in logging operations from child labor laws.\n#### 1. Short title\nThis Act may be cited as the Future Logging Careers Act .\n#### 2. Child labor law exemptions for logging operations\nThe Fair Labor Standards Act of 1938 ( 29 U.S.C. 201 et seq. ) is amended\u2014\n**(1)**\nin section 3 ( 29 U.S.C. 203 ), by adding at the end the following:\n(z) Logging operation \u2014 (1) means\u2014 (A) a mechanized operation; (B) the bucking or converting of timber into logs, poles, ties, bolts, pulpwood, chemical wood, excelsior wood, cordwood, fence posts, or similar products; (C) the collecting, skidding, yarding, loading, transporting, or unloading of such products in connection with the activities described in this paragraph; (D) the constructing, repairing, or maintaining of\u2014 (i) roads or camps used in connection with the activities described in this paragraph; or (ii) machinery or equipment used in the activities described in this paragraph; or (E) any other work performed in connection with the activities described in this paragraph; and (2) does not include the manual use of chainsaws to fell or process timber or the use of cable skidders to bring the timber to the landing. (aa) Mechanized operation \u2014 (1) means the felling, skidding, yarding, loading, or processing of timber by equipment other than manually operated chainsaws or cable skidders; and (2) includes the use of whole tree processors, cut-to-length processors, stroke boom delimbers, wheeled and track feller-bunchers, pull-through delimbers, wheeled and track forwarders, chippers, grinders, mechanical debarkers, wheeled and track grapple skidders, yarders, bulldozers, excavators, and log loaders. ; and\n**(2)**\nin section 13(c) ( 29 U.S.C. 213(c) ), by adding at the end the following:\n(8) The provisions of section 12 relating to child labor shall apply to an employee who is 16 or 17 years old employed in a logging operation in an occupation that the Secretary of Labor finds and declares to be particularly hazardous for the employment of children ages 16 or 17, except where such employee is employed by his parent or by a person standing in the place of his parent in a logging operation owned or operated by such parent or person. .",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "name": "Labor and Employment",
        "updateDate": "2025-03-12T17:02:57Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s509is.xml"
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
      "title": "Future Logging Careers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Future Logging Careers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to exempt certain 16- and 17-year-old individuals employed in logging operations from child labor laws.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:44Z"
    }
  ]
}
```
