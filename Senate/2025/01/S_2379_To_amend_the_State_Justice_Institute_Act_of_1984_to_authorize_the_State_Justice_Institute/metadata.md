# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2379
- Title: Countering Threats and Attacks on Our Judges Act
- Congress: 119
- Bill type: S
- Bill number: 2379
- Origin chamber: Senate
- Introduced date: 2025-07-22
- Update date: 2026-04-06T15:40:11Z
- Update date including text: 2026-04-06T15:40:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-22: Introduced in Senate
- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398-8399; text: CR S8398-8399)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-20 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 17:44:06 - Floor: Received in the House.
- 2025-11-20 18:18:43 - Floor: Held at the desk.
- Latest action: 2025-07-22: Introduced in Senate

## Actions

- 2025-07-22 - IntroReferral: Introduced in Senate
- 2025-07-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-11-20 - Floor: Message on Senate action sent to the House.
- 2025-11-20 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398-8399; text: CR S8398-8399)
- 2025-11-20 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-11-20 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-11-20 17:44:06 - Floor: Received in the House.
- 2025-11-20 18:18:43 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-22",
    "latestAction": {
      "actionDate": "2025-07-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2379",
    "number": "2379",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Countering Threats and Attacks on Our Judges Act",
    "type": "S",
    "updateDate": "2026-04-06T15:40:11Z",
    "updateDateIncludingText": "2026-04-06T15:40:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-11-20",
      "actionTime": "18:18:43",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-11-20",
      "actionTime": "17:44:06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8398-8399; text: CR S8398-8399)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-11-20",
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
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-07-22",
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
            "date": "2025-11-20T21:45:40Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-07-22T18:58:10Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "DE"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "KS"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "MO"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "RI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NH"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "WY"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "GA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-10-07",
      "state": "SD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "IN"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2379is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2379\nIN THE SENATE OF THE UNITED STATES\nJuly 22, 2025 Mr. Cornyn (for himself, Mr. Coons , Mr. Moran , Mr. Hawley , Mr. Whitehouse , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the State Justice Institute Act of 1984 to authorize the State Justice Institute to provide awards to certain organizations to establish a State judicial threat intelligence and resource center.\n#### 1. Short title\nThis Act may be cited as the Countering Threats and Attacks on Our Judges Act .\n#### 2. Definitions\nSection 202 of the State Justice Institute Act of 1984 ( 42 U.S.C. 10701 ) is amended\u2014\n**(1)**\nin paragraph (7), by striking and at the end;\n**(2)**\nin paragraph (8)(B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(9) eligible organization means a national nonprofit organization that\u2014 (A) provides technical assistance and training on, and has expertise and national-level experience in, judicial security and safety at the State and local levels; (B) has experience in courthouse design and courthouse security design standards; (C) has an understanding of State judicial operations and public access to judicial services; and (D) has experience working with a wide array of different judges and court systems, including an understanding of the challenges facing trial courts, appellate courts, rural courts, and limited-jurisdiction courts at the State and local levels. .\n#### 3. Establishment of State judicial threat intelligence and resource center\nSection 206(c) of the State Justice Institute Act of 1984 ( 42 U.S.C. 10705(c) ) is amended\u2014\n**(1)**\nin paragraph (14), by striking and at the end;\n**(2)**\nby redesignating paragraph (15) as paragraph (16); and\n**(3)**\nby inserting after paragraph (14) the following:\n(15) to provide financial and technical support to eligible organizations to establish, implement, and operate a State judicial threat and intelligence resource center to\u2014 (A) provide technical assistance and training around judicial security, including\u2014 (i) providing judicial officer safety education and training for judicial officers, courts, and local law enforcement; (ii) creating resources and guides around judicial security; and (iii) providing physical security assessments for courts, homes, and other facilities where judicial officers and staff conduct court-related business; (B) proactively monitor threats to the safety of State and local judges and court staff; (C) coordinate with Federal, State, and local law enforcement agencies to mitigate threats to the safety of State and local judges and court staff; (D) develop standardized incident reporting and threat evaluation practices for State and local courts in coordination with State and local law enforcement and fusion centers; (E) develop a national database for reporting, tracking, and sharing information about threats and incidents towards judicial officers and court staff at local and State levels with entities working in the interest of judicial security, including State and local law enforcement and fusion centers; and (F) coordinate research to identify, examine, and advance best practices around judicial security. .\n#### 4. Reports\nNot later than 1 year after the date on which a State judicial threat intelligence and resource center is established under paragraph (15) of section 206(c) of the State Justice Institute Act of 1984, as added by section 3 of this Act, the State Justice Institute shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives an annual report on the number of threats to State and local judiciary members and court staff, with breakdown of types of threats and level of seriousness.",
      "versionDate": "2025-07-22",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2379es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 2379\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo amend the State Justice Institute Act of 1984 to authorize the State Justice Institute to provide awards to certain organizations to establish a State judicial threat intelligence and resource center.\n#### 1. Short title\nThis Act may be cited as the Countering Threats and Attacks on Our Judges Act .\n#### 2. Definitions\nSection 202 of the State Justice Institute Act of 1984 ( 42 U.S.C. 10701 ) is amended\u2014\n**(1)**\nin paragraph (7), by striking and at the end;\n**(2)**\nin paragraph (8)(B), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(9) eligible organization means a national nonprofit organization that\u2014 (A) provides technical assistance and training on, and has expertise and national-level experience in, judicial security and safety at the State and local levels; (B) has experience in courthouse design and courthouse security design standards; (C) has an understanding of State judicial operations and public access to judicial services; and (D) has experience working with a wide array of different judges and court systems, including an understanding of the challenges facing trial courts, appellate courts, rural courts, and limited-jurisdiction courts at the State and local levels. .\n#### 3. Establishment of State judicial threat intelligence and resource center\nSection 206(c) of the State Justice Institute Act of 1984 ( 42 U.S.C. 10705(c) ) is amended\u2014\n**(1)**\nin paragraph (14), by striking and at the end;\n**(2)**\nby redesignating paragraph (15) as paragraph (16); and\n**(3)**\nby inserting after paragraph (14) the following:\n(15) to provide financial and technical support to eligible organizations to establish, implement, and operate a State judicial threat and intelligence resource center to\u2014 (A) provide technical assistance and training around judicial security, including\u2014 (i) providing judicial officer safety education and training for judicial officers, courts, and local law enforcement; (ii) creating resources and guides around judicial security; and (iii) providing physical security assessments for courts, homes, and other facilities where judicial officers and staff conduct court-related business; (B) proactively monitor threats to the safety of State and local judges and court staff; (C) coordinate with Federal, State, and local law enforcement agencies to mitigate threats to the safety of State and local judges and court staff; (D) develop standardized incident reporting and threat evaluation practices for State and local courts in coordination with State and local law enforcement and fusion centers; (E) develop a national database for reporting, tracking, and sharing information about threats and incidents towards judicial officers and court staff at local and State levels with entities working in the interest of judicial security, including State and local law enforcement and fusion centers; and (F) coordinate research to identify, examine, and advance best practices around judicial security. .\n#### 4. Reports\nNot later than 1 year after the date on which a State judicial threat intelligence and resource center is established under paragraph (15) of section 206(c) of the State Justice Institute Act of 1984, as added by section 3 of this Act, the State Justice Institute shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives an annual report on the number of threats to State and local judiciary members and court staff, with breakdown of types of threats and level of seriousness.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-07-22",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "4602",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Countering Threats and Attacks on Our Judges Act",
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
            "name": "Congressional oversight",
            "updateDate": "2025-11-21T19:59:58Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-11-21T19:59:58Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-11-21T19:59:58Z"
          },
          {
            "name": "Judges",
            "updateDate": "2025-11-21T19:59:58Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-11-21T19:59:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-09-12T16:25:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-20",
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
          "measure-id": "id119s2379",
          "measure-number": "2379",
          "measure-type": "s",
          "orig-publish-date": "2025-11-20",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2379v55",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-11-20",
          "action-desc": "Passed Senate",
          "summary-text": "<p><strong>Countering Threats and Attacks on Our Judges Act</strong></p><p>This bill allows funds awarded by the State Justice Institute to be used to establish, implement, and operate a judicial threat and intelligence resource center. The State Justice Institute is a private, nonprofit corporation established by federal law to support and improve the administration of justice in state courts.\u00a0</p>"
        },
        "title": "Countering Threats and Attacks on Our Judges Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2379.xml",
    "summary": {
      "actionDate": "2025-11-20",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Countering Threats and Attacks on Our Judges Act</strong></p><p>This bill allows funds awarded by the State Justice Institute to be used to establish, implement, and operate a judicial threat and intelligence resource center. The State Justice Institute is a private, nonprofit corporation established by federal law to support and improve the administration of justice in state courts.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2379"
    },
    "title": "Countering Threats and Attacks on Our Judges Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-20",
      "actionDesc": "Passed Senate",
      "text": "<p><strong>Countering Threats and Attacks on Our Judges Act</strong></p><p>This bill allows funds awarded by the State Justice Institute to be used to establish, implement, and operate a judicial threat and intelligence resource center. The State Justice Institute is a private, nonprofit corporation established by federal law to support and improve the administration of justice in state courts.\u00a0</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s2379"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2379is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2379es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Countering Threats and Attacks on Our Judges Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T11:58:21Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Countering Threats and Attacks on Our Judges Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-11-21T05:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Countering Threats and Attacks on Our Judges Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the State Justice Institute Act of 1984 to authorize the State Justice Institute to provide awards to certain organizations to establish a State judicial threat intelligence and resource center.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:26Z"
    }
  ]
}
```
