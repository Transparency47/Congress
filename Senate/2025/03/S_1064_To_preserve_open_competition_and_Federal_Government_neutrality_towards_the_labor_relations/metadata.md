# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1064
- Title: FOCA Act
- Congress: 119
- Bill type: S
- Bill number: 1064
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2025-12-05T21:34:02Z
- Update date including text: 2025-12-05T21:34:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1064",
    "number": "1064",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "FOCA Act",
    "type": "S",
    "updateDate": "2025-12-05T21:34:02Z",
    "updateDateIncludingText": "2025-12-05T21:34:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T22:30:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "AL"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TX"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TN"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "ID"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "NC"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "MS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "ND"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "AL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "OK"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "SC"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "IA"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "TN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "ID"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-04",
      "state": "LA"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "SC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "IN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "MS"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "SD"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1064is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1064\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Young (for himself, Mr. Tuberville , Mr. Cruz , Mr. Cornyn , Mr. Hagerty , Mr. Crapo , Mr. Budd , Ms. Lummis , Mr. Wicker , Mr. Cramer , Mrs. Britt , Mr. Lankford , Mr. Graham , Mr. Grassley , Mrs. Blackburn , Mr. Risch , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo preserve open competition and Federal Government neutrality towards the labor relations of Federal Government contractors on Federal and federally funded construction projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair and Open Competition Act or the FOCA Act .\n#### 2. Purposes\nIt is the purpose of this Act to\u2014\n**(1)**\npromote and ensure open competition on Federal and federally funded or assisted construction projects;\n**(2)**\nmaintain Federal Government neutrality towards the labor relations of Federal Government contractors on Federal and federally funded or assisted construction projects;\n**(3)**\nreduce construction costs to the Federal Government and to the taxpayers;\n**(4)**\nexpand job opportunities, especially for small and disadvantaged businesses; and\n**(5)**\nprevent discrimination against Federal Government contractors or their employees based upon labor affiliation or the lack thereof, thereby promoting the economical, nondiscriminatory, and efficient administration and completion of Federal and federally funded or assisted construction projects.\n#### 3. Preservation of open competition and Federal Government neutrality\n##### (a) Prohibition\n**(1) General rule**\nThe head of each executive agency that awards or enters into any construction contract or that obligates funds pursuant to such a contract, shall ensure that the agency, and any construction manager acting on behalf of the Federal Government with respect to such contract, in its bid specifications, project agreements, or other controlling documents does not\u2014\n**(A)**\nrequire or prohibit a bidder, offeror, contractor, or subcontractor from entering into, or adhering to, agreements with 1 or more labor organizations, with respect to that construction project or another related construction project; or\n**(B)**\ndiscriminate against or give preference to a bidder, offeror, contractor, or subcontractor because such bidder, offeror, contractor, or subcontractor\u2014\n**(i)**\nbecomes a signatory, or otherwise adheres to, an agreement with 1 or more labor organizations with respect to that construction project or another related construction project; or\n**(ii)**\nrefuses to become a signatory, or otherwise adhere to, an agreement with 1 or more labor organizations with respect to that construction project or another related construction project.\n**(2) Application of prohibition**\nThis subsection shall apply with respect to\u2014\n**(A)**\ncontracts awarded on or after the date of the enactment of this Act; and\n**(B)**\nsubcontracts awarded under such contracts.\n**(3) Rule of construction**\nNothing in paragraph (1) may be construed to prohibit a contractor or subcontractor from voluntarily entering into an agreement described in such paragraph.\n**(4) Federal acquisition regulation**\nNot later than 60 days after the date of the enactment of this Act, the Federal Acquisition Regulation shall be revised to implement the provisions of this subsection.\n##### (b) Recipients of grants and other assistance\nThe head of each executive agency that awards grants, provides financial assistance, or enters into cooperative agreements for construction projects after the date of the enactment of this Act shall ensure that\u2014\n**(1)**\nthe bid specifications, project agreements, or other controlling documents for such construction projects of a recipient of a grant or financial assistance, or by the parties to a cooperative agreement, do not contain any of the requirements or prohibitions described in subparagraph (A) or (B) of subsection (a)(1); or\n**(2)**\nthe bid specifications, project agreements, or other controlling documents for such construction projects of a construction manager acting on behalf of a recipient or party described in paragraph (1) do not contain any of the requirements or prohibitions described in subparagraph (A) or (B) of subsection (a)(1).\n##### (c) Failure To comply\nIf an executive agency, a recipient of a grant or financial assistance from an executive agency, a party to a cooperative agreement with an executive agency, or a construction manager acting on behalf of such an agency, recipient, or party, fails to comply with subsection (a) or (b), the head of the executive agency awarding the contract, grant, or assistance, or entering into the agreement involved, shall take such action, consistent with the law, as the head of such agency determines to be appropriate.\n##### (d) Exemptions\n**(1) In general**\nThe head of an executive agency may exempt a particular project, contract, subcontract, grant, or cooperative agreement from the requirements of 1 or more of the provisions of subsections (a) and (b) if the head of such agency determines that special circumstances exist that require an exemption in order to avert an imminent threat to public health or safety or to serve the national security.\n**(2) Special circumstances**\nFor purposes of paragraph (1), a finding of special circumstances may not be based on the possibility or existence of a labor dispute concerning contractors or subcontractors that are nonsignatories to, or that otherwise do not adhere to, agreements with 1 or more labor organizations, or labor disputes concerning employees on the project who are not members of, or affiliated with, a labor organization.\n**(3) Additional exemption for certain projects**\nThe head of an executive agency, upon application of an awarding authority, a recipient of grants or financial assistance, a party to a cooperative agreement, or a construction manager acting on behalf of any of such entities, may exempt a particular project from the requirements of any or all of the provisions of subsection (a) or (b), if the head of such agency finds\u2014\n**(A)**\nthat the awarding authority, recipient of grants or financial assistance, party to a cooperative agreement, or construction manager acting on behalf of any of such entities had issued or was a party to, as of the date of the enactment of this Act, bid specifications, project agreements, agreements with 1 or more labor organizations, or other controlling documents with respect to that particular project, which contained any of the requirements or prohibitions set forth in subsection (a)(1); and\n**(B)**\nthat 1 or more construction contracts subject to such requirements or prohibitions had been awarded as of the date of the enactment of this Act.\n##### (e) Definitions\nIn this section:\n**(1) Construction contract**\nThe term construction contract means any contract for the construction, rehabilitation, alteration, conversion, extension, or repair of buildings, highways, or other improvements to real property.\n**(2) Executive agency**\nThe term executive agency has the meaning given the term Executive agency in section 105 of title 5, United States Code, except that such term does not include the Government Accountability Office.\n**(3) Labor organization**\nThe term labor organization has the meaning given such term in section 701 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000e ).",
      "versionDate": "2025-03-13",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "2126",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FOCA Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T15:21:25Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1064is.xml"
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
      "title": "FOCA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FOCA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair and Open Competition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to preserve open competition and Federal Government neutrality towards the labor relations of Federal Government contractors on Federal and federally funded construction projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:26Z"
    }
  ]
}
```
