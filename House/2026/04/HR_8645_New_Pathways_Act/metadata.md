# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8645?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8645
- Title: New Pathways Act
- Congress: 119
- Bill type: HR
- Bill number: 8645
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T22:29:05Z
- Update date including text: 2026-05-19T22:29:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8645",
    "number": "8645",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000822",
        "district": "12",
        "firstName": "Bonnie",
        "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
        "lastName": "Watson Coleman",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "New Pathways Act",
    "type": "HR",
    "updateDate": "2026-05-19T22:29:05Z",
    "updateDateIncludingText": "2026-05-19T22:29:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "NJ"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8645ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8645\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mrs. Watson Coleman (for herself, Ms. Vel\u00e1zquez , Mr. Johnson of Georgia , Ms. Norton , Ms. Tlaib , Mr. Davis of Illinois , Mrs. McIver , and Mr. Green of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Second Chance Act of 2007 to require identification for returning citizens, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Pathways Act .\n#### 2. Identification for returning citizens\nSection 231(b) of the Second Chance Act of 2007 ( 34 U.S.C. 60541(b) ) is amended to read as follows:\n(b) Identification and release assistance for Federal prisoners (1) Definitions In this subsection\u2014 (A) the term community confinement means residence in a community treatment center, halfway house, restitution center, mental health facility, alcohol or drug rehabilitation center, or other community facility; (B) the term direct-release prisoner means a prisoner who is scheduled for release and will not be placed in prerelease custody; (C) the term noncitizen covered individual \u2014 (i) means an individual in the custody of the Bureau of Prisons or sentenced to a term in community confinement who\u2014 (I) is lawfully present and eligible for employment authorization in the United States; and (II) has a document demonstrating that the individual will have a place of residence upon release; and (ii) includes an alien lawfully admitted for permanent residence (as defined in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) )), a refugee (as defined in that section of that Act), and an asylee; and (D) the term United States citizen covered individual means an individual in the custody of the Bureau of Prisons or sentenced to a term in community confinement who has\u2014 (i) a social security card; (ii) a document described in paragraph (2)(B)(ii) as proof of United States citizenship; and (iii) a document demonstrating that the individual will have a place of residence upon release. (2) Obtaining identification for United States citizens (A) In general With respect to a United States citizen covered individual, the Director shall provide a photo identification card, which shall comply with the minimum requirements described in section 202(b) of the REAL ID Act of 2005 ( 49 U.S.C. 30301 note), prior to\u2014 (i) the release of the United States citizen covered individual from a term of imprisonment in a Federal prison; or (ii) the release of the United States citizen covered individual from a sentence to a term in community confinement. (B) Assistance in obtaining documents (i) In general Subject to clause (iii), for the purpose of issuing an identification card under this subsection, the Director shall obtain, on behalf of United States citizen covered individuals\u2014 (I) a social security card; and (II) a document described in clause (ii) as proof of United States citizenship. (ii) Proof of United States citizenship A document described in this clause is\u2014 (I) a United States passport; (II) an original or certified copy of a birth certificate that indicates that the individual was born in the United States or a territory of the United States; (III) in the case of a United States citizen born inside the United States for whom a document described in subclause (I) or (II) is not available, any document described in subsection (a), (b), or (c) of section 435.407 of title 42, Code of Federal Regulations, or any successor thereto; or (IV) in the case of a United States citizen born outside the United States, an original or certified copy of\u2014 (aa) a certificate of naturalization (Form N\u2013550 or N\u2013570); (bb) a consular report of birth abroad (Form FS\u2013240); (cc) a certification of birth abroad (Form FS\u2013545); (dd) a certification of report of birth (Form DS\u20131350); or (ee) a certificate of citizenship (Form N\u2013560). (iii) Exceptions (I) Lack of response from Federal or State agency If the Director cannot obtain a copy of a document required under clause (i) because of inaction by the Federal or State agency from which the document was requested, the Director shall provide to the United States citizen covered individual\u2014 (aa) a written statement that explains what steps the Director took in trying to obtain the document; and (bb) any documents transmitted to the Director by the Federal or State agency in response to the request for the document. (II) Lack of authorization from United States citizen covered individual If the Director cannot obtain a copy of a document required under clause (i) because the United States citizen covered individual does not provide the authorization required to obtain the document, the Director shall provide a written statement to the United States citizen covered individual that explains why the document was not obtained. (C) Provision of documents Upon issuance of an identification card to a covered individual under this paragraph, the Director shall provide all documents obtained for the United States citizen covered individual under subparagraph (B). (3) Obtaining documents for noncitizens (A) In general With respect to a noncitizen covered individual, the Director shall assist in obtaining from the Director of the U.S. Citizenship and Immigration Services\u2014 (i) proof of lawful status in the United States of the noncitizen covered individual; and (ii) in the case of a noncitizen covered individual who is not admitted for lawful permanent residence, an employment authorization document. (B) Assistance The assistance provided by the Director under subparagraph (A) shall include\u2014 (i) providing the noncitizen covered individual with applicable U.S. Citizenship and Immigration Services forms and instructions; and (ii) assisting the noncitizen covered individual in completing and submitting such forms, together with any required supporting documentation. (C) Provision of documents Upon receipt of a document for a noncitizen covered individual under this paragraph, the Director shall provide such document to the noncitizen covered individual. (4) Assistance developing release plan At the request of a direct-release prisoner, a representative of the United States Probation System shall, prior to the release of that prisoner, help that prisoner develop a release plan. .",
      "versionDate": "2026-04-30",
      "versionType": "Introduced in House"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-05-19T22:29:05Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8645ih.xml"
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
      "title": "New Pathways Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "New Pathways Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Second Chance Act of 2007 to require identification for returning citizens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:35Z"
    }
  ]
}
```
