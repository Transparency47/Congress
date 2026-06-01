# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/137
- Title: A bill to amend title 41, United States Code, to prohibit the Federal Government from entering into contracts with an entity that discriminates against firearm or ammunition industries, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 137
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-02-25T11:56:37Z
- Update date including text: 2026-02-25T11:56:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/137",
    "number": "137",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000618",
        "district": "",
        "firstName": "Steve",
        "fullName": "Sen. Daines, Steve [R-MT]",
        "lastName": "Daines",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "A bill to amend title 41, United States Code, to prohibit the Federal Government from entering into contracts with an entity that discriminates against firearm or ammunition industries, and for other purposes.",
    "type": "S",
    "updateDate": "2026-02-25T11:56:37Z",
    "updateDateIncludingText": "2026-02-25T11:56:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
            "date": "2025-01-16T21:33:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T21:33:46Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MS"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AR"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "LA"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NE"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AL"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "IA"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MO"
    },
    {
      "bioguideId": "G000359",
      "firstName": "Lindsey",
      "fullName": "Sen. Graham, Lindsey [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Graham",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ND"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-01-27",
      "state": "UT"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "WV"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "OH"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "PA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s137is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 137\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Daines (for himself, Mrs. Hyde-Smith , Ms. Lummis , Mr. Scott of Florida , Mr. Cotton , Mr. Marshall , Mr. Risch , Mr. Wicker , Mr. Cramer , Mrs. Fischer , Mr. Budd , Mr. Cassidy , Mr. Crapo , Mr. Sheehy , Mr. Ricketts , Mrs. Britt , Mr. Lankford , Ms. Ernst , Mr. Schmitt , Mr. Graham , Mr. Hoeven , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 41, United States Code, to prohibit the Federal Government from entering into contracts with an entity that discriminates against firearm or ammunition industries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Firearm Industry Non-Discrimination Act or the FIND Act .\n#### 2. Prohibition on entering into contracts with entities discriminating against firearm or ammunition industries\n##### (a) Prohibition\nChapter 47 of title 41, United States Code, is amended by adding at the end the following:\n4715. Prohibition on entering into contracts with entities discriminating against firearm or ammunition industries. (a) Prohibition (1) In general The head of an executive agency shall include in each contract for the procurement of goods or services awarded by the executive agency, a clause requiring the prime contractor to certify that the contractor\u2014 (A) has no policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association; and (B) will not adopt a policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association during the term of the contract. (2) Subcontracts The head of an executive agency shall include in each contract for the procurement of goods or services awarded by the executive agency, a clause that prohibits the prime contractor on such contract from\u2014 (A) awarding a first-tier subcontract with a value greater than 10 percent of the total value of the prime contract to an entity that fails to certify in writing to the prime contractor that the entity\u2014 (i) has no policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association; and (ii) will not adopt a policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association during the term of the contract; and (B) structuring subcontract tiers in a manner designed to avoid violating subparagraph (A) by enabling a subcontractor to perform more than 10 percent of the total value of the prime contract as a lower-tier subcontractor. (3) Penalties The clause included in contracts pursuant to paragraph (1) or paragraph (2) shall provide that, in the event that the prime contractor violates the clause\u2014 (A) the prime contract shall be terminated for default; and (B) a suspension or debarment proceeding will be initiated for the contractor on the basis of the violation. (b) Exception Subsection (a) shall not apply to a contract for the procurement of goods or services that is a sole-source contract. (c) Definitions In this section: (1) Discriminate The term discriminate means to\u2014 (A) make a judgement about a policy, practice, guidance, or directive on the basis of\u2014 (i) partial criteria or a category-based assessment analysis, rather than\u2014 (I) on a case-by-case basis; or (II) using empirical data evaluated under quantifiable standards; or (ii) criteria other than criteria free from\u2014 (I) favoritism or prejudice against or dislike for the firearm entity or trade association or the products or services sold by the firearm entity or trade association; or (II) favoritism for market alternatives to the business of the firearm entity or the trade association; (B) refuse to provide services, or deny, cancel, or limit services, to the firearm entity or trade association on the basis of criteria other than\u2014 (i) criteria free from\u2014 (I) favoritism or prejudice against or dislike for the firearm entity or trade association or the products or services sold by the firearm entity or trade association; or (II) favoritism for market alternatives to the business of the firearm entity or the trade association; (ii) criteria related to credit history and financial risk specific to a customer or potential customer; or (iii) criteria related to noncompliance with Federal, State, or local law; or (C) limit the operations of the firearm entity or trade association in manner not required by\u2014 (i) Federal, State, or local law; or (ii) Federal, State, or local regulation. (2) Firearm entity The term firearm entity means any\u2014 (A) person who is licensed under section 923 of title 18 to import, manufacture, or deal in firearms; (B) seller of ammunition, as defined in section 7903 of title 15; (C) manufacturer or importer of, or dealer in, a secure gun storage or safety device, as defined in section 921(a) of title 18; and (D) manufacturer or importer of, or dealer in, a component part or accessory of a firearm or ammunition. (3) Firearm trade association The term firearm trade association has the meaning in section 7903 of title 15. (4) First-tier subcontract The term first-tier subcontract means a subcontract entered into by a subcontractor with the prime contractor for the purposes of carrying out the prime contract. (5) Lower-tier subcontractor The term lower-tier subcontractor means any person entering into a contract with a subcontractor of a prime contractor for the purposes of carrying out the prime contract. (6) Prime contract; prime contractor The terms prime contract and prime contractor have the meaning given those terms in section 8701 of title 41. .\n##### (b) Application\nSection 4715 of title 41, United States Code, as added by subsection (a), shall apply with respect to contracts awarded on or after the date of the enactment of this Act.\n##### (c) Clerical amendment\nThe table of sections for chapter 47 of title 41, United States Code, is amended by adding at the end the following:\n4715. Prohibition on entering into contracts with entities discriminating against firearm or ammunition industries. .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "45",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "FIND Act",
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
            "name": "Firearms and explosives",
            "updateDate": "2025-03-03T17:35:13Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-03-03T17:35:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-03-10T15:56:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s137",
          "measure-number": "137",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s137v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Firearm Industry Non-Discrimination Act or the FIND Act</strong></p> <p>This bill prohibits the federal government from entering into contracts with an entity that discriminates against firearm trade associations or businesses that deal in firearms, ammunition, or related products.</p> <p> Specifically, the bill requires a federal agency to include in each contract for the procurement of goods or services awarded by the agency a clause requiring the prime contractor to certify that it (1) has no policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association; and (2) will not adopt a policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association during the term of the contract.</p> <p>The bill establishes (1) a similar requirement with respect to subcontracts, and (2) penalties for violations.</p> <p>The bill makes such prohibition inapplicable to a contract for the procurement of goods or services that is a sole-source contract. </p>"
        },
        "title": "FIND Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s137.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Industry Non-Discrimination Act or the FIND Act</strong></p> <p>This bill prohibits the federal government from entering into contracts with an entity that discriminates against firearm trade associations or businesses that deal in firearms, ammunition, or related products.</p> <p> Specifically, the bill requires a federal agency to include in each contract for the procurement of goods or services awarded by the agency a clause requiring the prime contractor to certify that it (1) has no policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association; and (2) will not adopt a policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association during the term of the contract.</p> <p>The bill establishes (1) a similar requirement with respect to subcontracts, and (2) penalties for violations.</p> <p>The bill makes such prohibition inapplicable to a contract for the procurement of goods or services that is a sole-source contract. </p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s137"
    },
    "title": "FIND Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Firearm Industry Non-Discrimination Act or the FIND Act</strong></p> <p>This bill prohibits the federal government from entering into contracts with an entity that discriminates against firearm trade associations or businesses that deal in firearms, ammunition, or related products.</p> <p> Specifically, the bill requires a federal agency to include in each contract for the procurement of goods or services awarded by the agency a clause requiring the prime contractor to certify that it (1) has no policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association; and (2) will not adopt a policy, practice, guidance, or directive that discriminates against a firearm entity or firearm trade association during the term of the contract.</p> <p>The bill establishes (1) a similar requirement with respect to subcontracts, and (2) penalties for violations.</p> <p>The bill makes such prohibition inapplicable to a contract for the procurement of goods or services that is a sole-source contract. </p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s137"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s137is.xml"
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
      "title": "FIND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FIND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Firearm Industry Non-Discrimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 41, United States Code, to prohibit the Federal Government from entering into contracts with an entity that discriminates against firearm or ammunition industries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T03:18:19Z"
    }
  ]
}
```
