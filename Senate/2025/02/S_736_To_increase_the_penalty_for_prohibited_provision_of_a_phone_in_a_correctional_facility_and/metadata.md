# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/736?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/736
- Title: Lieutenant Osvaldo Albarati Stopping Prison Contraband Act
- Congress: 119
- Bill type: S
- Bill number: 736
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-05-22T19:48:25Z
- Update date including text: 2026-05-22T19:48:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 410.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2026-05-14 - Committee: Committee on the Judiciary. Ordered to be reported without amendment favorably.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Committee: Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.
- 2026-05-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 410.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/736",
    "number": "736",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act",
    "type": "S",
    "updateDate": "2026-05-22T19:48:25Z",
    "updateDateIncludingText": "2026-05-22T19:48:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 410.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-19",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on the Judiciary. Reported by Senator Grassley without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on the Judiciary. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
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
            "date": "2026-05-19T18:51:03Z",
            "name": "Reported By"
          },
          {
            "date": "2026-05-14T17:58:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-26T16:42:31Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-26T16:42:31Z",
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
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "ID"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TN"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "SC"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-18",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "HI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "CA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "VT"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-18",
      "state": "IL"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s736is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 736\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Grassley (for himself, Mr. Ossoff , Mrs. Hyde-Smith , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo increase the penalty for prohibited provision of a phone in a correctional facility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lieutenant Osvaldo Albarati Stopping Prison Contraband Act .\n#### 2. Prohibited provision of a phone\nSection 1791(b) of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (4) and (5) as paragraphs (5) and (6), respectively;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) in the case of a violation of subsection (a)(1), imprisonment for not more than 2 years, or both, if the object is specified in subsection (d)(1)(F) of this section; ; and\n**(3)**\nin paragraph (5), as so redesignated, by inserting , in the case of a violation of subsection (a)(2), before (d)(1)(F) .\n#### 3. Review of policies\nNot later than 1 year after the date of enactment of this Act, the Director of the Bureau of Prisons shall\u2014\n**(1)**\nconduct a review of the policies of the Bureau of Prisons pertaining to inmates who make, possess, obtain, or attempt to make or obtain a prohibited object, as defined in section 1791(d)(1) of title 18, United States Code; and\n**(2)**\nupdate those policies as needed to improve protections for incarcerated individuals and staff.",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s736rs.xml",
      "text": "II\nCalendar No. 410\n119th CONGRESS\n2d Session\nS. 736\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Grassley (for himself, Mr. Ossoff , Mrs. Hyde-Smith , Mr. Booker , Mr. Cruz , Mr. Crapo , Mrs. Moody , Mrs. Blackburn , Mr. Graham , Ms. Klobuchar , Mr. Tillis , Ms. Hirono , Mr. Blumenthal , Mr. Padilla , Mr. Welch , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nMay 19, 2026 Reported by Mr. Grassley , without amendment\nA BILL\nTo increase the penalty for prohibited provision of a phone in a correctional facility, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lieutenant Osvaldo Albarati Stopping Prison Contraband Act .\n#### 2. Prohibited provision of a phone\nSection 1791(b) of title 18, United States Code, is amended\u2014\n**(1)**\nby redesignating paragraphs (4) and (5) as paragraphs (5) and (6), respectively;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) in the case of a violation of subsection (a)(1), imprisonment for not more than 2 years, or both, if the object is specified in subsection (d)(1)(F) of this section; ; and\n**(3)**\nin paragraph (5), as so redesignated, by inserting , in the case of a violation of subsection (a)(2), before (d)(1)(F) .\n#### 3. Review of policies\nNot later than 1 year after the date of enactment of this Act, the Director of the Bureau of Prisons shall\u2014\n**(1)**\nconduct a review of the policies of the Bureau of Prisons pertaining to inmates who make, possess, obtain, or attempt to make or obtain a prohibited object, as defined in section 1791(d)(1) of title 18, United States Code; and\n**(2)**\nupdate those policies as needed to improve protections for incarcerated individuals and staff.",
      "versionDate": "2026-05-19",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-05-13",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "3353",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act",
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
            "updateDate": "2025-07-24T17:58:45Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-07-24T17:58:45Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-07-24T17:58:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T14:10:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119s736",
          "measure-number": "736",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s736v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Lieutenant Osvaldo Albarati Stopping Prison Contraband Act</strong></p><p>This bill increases federal criminal penalties for providing or attempting to provide a cell phone to an individual who is incarcerated at a prison.</p>"
        },
        "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s736.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Lieutenant Osvaldo Albarati Stopping Prison Contraband Act</strong></p><p>This bill increases federal criminal penalties for providing or attempting to provide a cell phone to an individual who is incarcerated at a prison.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s736"
    },
    "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Lieutenant Osvaldo Albarati Stopping Prison Contraband Act</strong></p><p>This bill increases federal criminal penalties for providing or attempting to provide a cell phone to an individual who is incarcerated at a prison.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s736"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s736is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s736rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T19:48:25Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-21T22:38:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lieutenant Osvaldo Albarati Stopping Prison Contraband Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the penalty for prohibited provision of a phone in a correctional facility, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:33Z"
    }
  ]
}
```
