# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/698
- Title: Federal Prisons Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 698
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2026-03-10T11:03:22Z
- Update date including text: 2026-03-10T11:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/698",
    "number": "698",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M000355",
        "district": "",
        "firstName": "Mitch",
        "fullName": "Sen. McConnell, Mitch [R-KY]",
        "lastName": "McConnell",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Federal Prisons Accountability Act of 2025",
    "type": "S",
    "updateDate": "2026-03-10T11:03:22Z",
    "updateDateIncludingText": "2026-03-10T11:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-24",
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
            "date": "2025-02-24T23:05:40Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-24T23:05:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "KY"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "OK"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TN"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "LA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "GA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s698is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 698\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. McConnell (for himself, Mr. Grassley , Mr. Paul , Mr. Lankford , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Director of the Bureau of Prisons to be appointed by and with the advice and consent of the Senate.\n#### 1. Short title\nThis Act may be cited as the Federal Prisons Accountability Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Director of the Bureau of Prisons leads a law enforcement component of the Department of Justice with a budget that exceeded $8,390,000,000 for fiscal year 2024.\n**(2)**\nWith the exception of the Federal Bureau of Investigation, the Bureau of Prisons had the largest operating budget of any unit within the Department of Justice for fiscal year 2024.\n**(3)**\nAs of 2025, the Director of the Bureau of Prisons oversaw 122 facilities and was responsible for the welfare of more than 155,000 Federal inmates.\n**(4)**\nAs of 2025, the Director of the Bureau of Prisons supervised more than 35,000 employees, many of whom operate in hazardous environments that involve regular interaction with violent offenders.\n**(5)**\nWithin the Department of Justice, in addition to those officials who oversee litigating components, the Director of the Bureau of Alcohol, Tobacco, Firearms and Explosives, the Director of the Community Relations Service, the Director of the Federal Bureau of Investigation, the Director of the Office on Violence Against Women, the Administrator of the Drug Enforcement Administration, the Deputy Administrator of the Drug Enforcement Administration, the Director of the United States Marshals Service, 94 United States Marshals, the Inspector General of the Department of Justice, and the Special Counsel for Immigration Related Unfair Employment Practices, are all appointed by the President by and with the advice and consent of the Senate.\n**(6)**\nDespite the significant budget of the Bureau of Prisons and the vast number of people under the responsibility of the Director of the Bureau of Prisons, the Director is not appointed by and with the advice and consent of the Senate.\n#### 3. Director of the Bureau of Prisons\n##### (a) In general\nSection 4041 of title 18, United States Code, is amended by striking appointed by and serving directly under the Attorney General. and inserting the following: who shall be appointed by the President, by and with the advice and consent of the Senate. The Director shall serve directly under the Attorney General. .\n##### (b) Incumbent\nNotwithstanding the amendment made by subsection (a), the individual serving as the Director of the Bureau of Prisons on the date of enactment of this Act may serve as the Director of the Bureau of Prisons until the date that is 3 months after the date of enactment of this Act.\n##### (c) Rule of construction\nNothing in this Act shall be construed to limit the ability of the President to appoint the individual serving as the Director of the Bureau of Prisons on the date of enactment of this Act to the position of Director of the Bureau of Prisons in accordance with section 4041 of title 18, United States Code, as amended by subsection (a).\n##### (d) Term\n**(1) In general**\nSection 4041 of title 18, United States Code, as amended by subsection (a), is amended by inserting after consent of the Senate. the following: The Director shall be appointed for a term of 10 years, except that an individual appointed to the position of Director may continue to serve in that position until another individual is appointed to that position, by and with the advice and consent of the Senate. An individual may not serve more than 1 term as Director. .\n**(2) Applicability**\nThe amendment made by paragraph (1) shall apply to appointments made on or after the date of enactment of this Act.",
      "versionDate": "2025-02-24",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4355",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Prisons Accountability Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Correctional facilities and imprisonment",
            "updateDate": "2025-07-17T20:29:16Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-07-17T20:29:12Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-07-17T20:29:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T15:02:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s698",
          "measure-number": "698",
          "measure-type": "s",
          "orig-publish-date": "2025-02-24",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s698v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Federal Prisons Accountability Act of 2025\u00a0</strong></p><p>This bill modifies the appointment procedures and term of service for the Director of the Bureau of Prisons.</p><p>Currently, the director is appointed by the Attorney General. This bill requires the director to be appointed by the President and confirmed by the Senate.</p><p>The bill also limits the director to a single term of 10 years.</p>"
        },
        "title": "Federal Prisons Accountability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s698.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Prisons Accountability Act of 2025\u00a0</strong></p><p>This bill modifies the appointment procedures and term of service for the Director of the Bureau of Prisons.</p><p>Currently, the director is appointed by the Attorney General. This bill requires the director to be appointed by the President and confirmed by the Senate.</p><p>The bill also limits the director to a single term of 10 years.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s698"
    },
    "title": "Federal Prisons Accountability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Federal Prisons Accountability Act of 2025\u00a0</strong></p><p>This bill modifies the appointment procedures and term of service for the Director of the Bureau of Prisons.</p><p>Currently, the director is appointed by the Attorney General. This bill requires the director to be appointed by the President and confirmed by the Senate.</p><p>The bill also limits the director to a single term of 10 years.</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s698"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s698is.xml"
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
      "title": "Federal Prisons Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Prisons Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the Bureau of Prisons to be appointed by and with the advice and consent of the Senate.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T03:48:24Z"
    }
  ]
}
```
