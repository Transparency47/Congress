# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/679?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/679
- Title: LEOSA Reform Act
- Congress: 119
- Bill type: S
- Bill number: 679
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-04-29T11:03:31Z
- Update date including text: 2026-04-29T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/679",
    "number": "679",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "LEOSA Reform Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:31Z",
    "updateDateIncludingText": "2026-04-29T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
            "date": "2025-02-20T23:24:27Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-20T23:24:27Z",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "MS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "TN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "TX"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WV"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TN"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2026-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "WV"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "OH"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s679is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 679\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Kennedy (for himself, Mr. Scott of Florida , Mrs. Hyde-Smith , Mr. Ricketts , Mr. Hagerty , Mr. Cornyn , Mr. Justice , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to improve the Law Enforcement Officers Safety Act of 2004 and provisions relating to the carrying of concealed weapons by law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the LEOSA Reform Act .\n#### 2. Conforming the Law Enforcement Officers Safety Act of 2004 and the Gun-Free School Zones Act of 1990\nSection 922(q) of title 18, United States Code, is amended\u2014\n**(1)**\nin paragraph (2)(B)\u2014\n**(A)**\nin clause (vi), by striking or at the end;\n**(B)**\nin clause (vii), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(viii) by an individual authorized by section 926B or 926C to carry a concealed firearm. ; and\n**(2)**\nin paragraph (3)(B)\u2014\n**(A)**\nin clause (iii), by striking or at the end;\n**(B)**\nin clause (iv), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(v) by an individual authorized by section 926B or 926C to carry a concealed firearm. .\n#### 3. Making improvements to the Law Enforcement Officers Safety Act of 2004\n##### (a) Carrying of concealed firearms by qualified law enforcement officers\nSection 926B of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by inserting , or any other provision of Federal law (including any regulation prescribed by the Secretary of the Interior pertaining to a unit of the National Park System) after thereof ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , except to the extent that the laws apply on property used by a common or contract carrier to transport people or property by land, rail, or water or on property open to the public (whether or not a fee is charged to enter the property) before the semicolon; and\n**(B)**\nin paragraph (2), by inserting , except to the extent that the laws apply on property used by a common or contract carrier to transport people or property by land, rail, or water or on property open to the public (whether or not a fee is charged to enter the property) before the period at the end; and\n**(3)**\nin subsection (e)(2), by inserting any magazine and after includes .\n##### (b) Carrying of concealed firearms by qualified retired law enforcement officers\nSection 926C of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), by inserting , or any other provision of Federal law (including any regulation prescribed by the Secretary of the Interior pertaining to a unit of the National Park System) after thereof ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by inserting , except to the extent that the laws apply on property used by a common or contract carrier to transport people or property by land, rail, or water or on property open to the public (whether or not a fee is charged to enter the property) before the semicolon; and\n**(B)**\nin paragraph (2), by inserting , except to the extent that the laws apply on property used by a common or contract carrier to transport people or property by land, rail, or water or on property open to the public (whether or not a fee is charged to enter the property) before the period;\n**(3)**\nby striking subsection (c)(4) and inserting the following:\n(4) during the most recent 12-month period (or, at the option of the State in which the individual resides, a greater number of months, not exceeding 36 months), has met\u2014 (A) the standards for active duty law enforcement officers, as established by the former agency of the individual; (B) the standards for active duty law enforcement officers, as established by the State in which the individual resides; (C) the standards for active duty law enforcement officers employed by any law enforcement agency in the State in which the individual resides; or (D) any standard for active duty law enforcement officers for firearms qualification conducted by any certified firearms instructor within the State in which the individual resides; ;\n**(4)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1), by striking not less recently than one year before the date the individual is carrying the concealed firearm, been tested or otherwise found by the agency to meet the active duty standards for qualification in firearms training as established by the agency to carry and inserting met the standards required by subsection (c)(4) for ; and\n**(B)**\nin paragraph (2), by striking subparagraph (B) and inserting the following:\n(B) a certification issued by the former agency of the individual, the State in which the individual resides, any law enforcement agency within the State in which the individual resides, or any certified firearms instructor within the State in which the individual resides that indicates that the individual has met the standards required by subsection (c)(4). ; and\n**(5)**\nin subsection (e)(1)(B), by inserting any magazine and after includes .\n#### 4. Permitting qualified current and retired law enforcement officers to carry firearms in certain Federal facilities\nSection 930 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (2), by striking or at the end;\n**(B)**\nin paragraph (3), by striking the period at the end and inserting or ; and\n**(C)**\nby adding at the end the following:\n(4) the possession of a firearm or ammunition in a Facility Security Level I or II civilian public access facility by a qualified law enforcement officer or a qualified retired law enforcement officer. ; and\n**(2)**\nin subsection (g), by adding at the end the following:\n(4) The term civilian public access facility means a facility open to the general public. (5) The term Facility Security Level means a security risk assessment level assigned to a Federal facility by the security agency of the facility in accordance with the biannually issued Interagency Security Committee Standard. (6) The term qualified law enforcement officer has the meaning given the term in section 926B. (7) The term qualified retired law enforcement officer has the meaning given the term in section 926C. .",
      "versionDate": "2025-02-20",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-10T17:35:30Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-07-10T17:35:36Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-07-10T17:35:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-09T21:11:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s679",
          "measure-number": "679",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2026-03-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s679v00",
            "update-date": "2026-03-23"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>LEOSA Reform Act</strong></p> <p>This bill broadens the authority for certain individuals to carry concealed firearms in school zones and across state lines. </p> <p>Specifically, the bill exempts the following categories of individuals from the federal prohibition on possessing (or discharging) a firearm in a school zone:</p> <ul> <li>certain active and retired law enforcement officers who are authorized to carry concealed firearms under federal law, and</li> <li>individuals who are allowed to carry concealed firearms under the law of a state. </li> </ul> <p>Additionally, the bill allows qualified active and retired law enforcement officers to carry concealed firearms and ammunition (including magazines) in national parks; on state, local, or private property that is open to the public; and in certain federal facilities that are open to the public.</p> <p>Finally, the bill permits states to reduce the frequency with which retired law enforcement officers must meet certain qualification standards. </p>"
        },
        "title": "LEOSA Reform Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s679.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>LEOSA Reform Act</strong></p> <p>This bill broadens the authority for certain individuals to carry concealed firearms in school zones and across state lines. </p> <p>Specifically, the bill exempts the following categories of individuals from the federal prohibition on possessing (or discharging) a firearm in a school zone:</p> <ul> <li>certain active and retired law enforcement officers who are authorized to carry concealed firearms under federal law, and</li> <li>individuals who are allowed to carry concealed firearms under the law of a state. </li> </ul> <p>Additionally, the bill allows qualified active and retired law enforcement officers to carry concealed firearms and ammunition (including magazines) in national parks; on state, local, or private property that is open to the public; and in certain federal facilities that are open to the public.</p> <p>Finally, the bill permits states to reduce the frequency with which retired law enforcement officers must meet certain qualification standards. </p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s679"
    },
    "title": "LEOSA Reform Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>LEOSA Reform Act</strong></p> <p>This bill broadens the authority for certain individuals to carry concealed firearms in school zones and across state lines. </p> <p>Specifically, the bill exempts the following categories of individuals from the federal prohibition on possessing (or discharging) a firearm in a school zone:</p> <ul> <li>certain active and retired law enforcement officers who are authorized to carry concealed firearms under federal law, and</li> <li>individuals who are allowed to carry concealed firearms under the law of a state. </li> </ul> <p>Additionally, the bill allows qualified active and retired law enforcement officers to carry concealed firearms and ammunition (including magazines) in national parks; on state, local, or private property that is open to the public; and in certain federal facilities that are open to the public.</p> <p>Finally, the bill permits states to reduce the frequency with which retired law enforcement officers must meet certain qualification standards. </p>",
      "updateDate": "2026-03-23",
      "versionCode": "id119s679"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s679is.xml"
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
      "title": "LEOSA Reform Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LEOSA Reform Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-15T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to improve the Law Enforcement Officers Safety Act of 2004 and provisions relating to the carrying of concealed weapons by law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:19Z"
    }
  ]
}
```
