# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5283
- Title: Healthcare Workforce Resilience Act
- Congress: 119
- Bill type: HR
- Bill number: 5283
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2026-05-22T08:08:41Z
- Update date including text: 2026-05-22T08:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5283",
    "number": "5283",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001190",
        "district": "10",
        "firstName": "Bradley",
        "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
        "lastName": "Schneider",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Healthcare Workforce Resilience Act",
    "type": "HR",
    "updateDate": "2026-05-22T08:08:41Z",
    "updateDateIncludingText": "2026-05-22T08:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T14:01:10Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "NE"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NC"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "MA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "WA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "OR"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "RI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "DC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "OR"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NM"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "KS"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5283ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5283\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mr. Schneider (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo enhance our Nation\u2019s nurse and physician workforce by recapturing unused immigrant visas.\n#### 1. Short title\nThis Act may be cited as the Healthcare Workforce Resilience Act .\n#### 2. Recapturing unused immigrant visas for professional nurses and physicians\nSection 106(d) of the American Competitiveness in the Twenty-first Century Act of 2000 (title I of Public Law 106\u2013313 ; 8 U.S.C. 1153 note) is amended to read as follows:\n(d) Recapture of unused employment-Based immigrant visas (1) In general Subject to paragraph (2), and notwithstanding any other provision of law, the number of employment-based visas made available under section 203(b) of the Immigration and Nationality Act ( 8 U.S.C. 1153(b) ) shall be increased by the number calculated in paragraph (3). (2) Limitations (A) In general Visas may only be made available under this subsection for up to 40,000 employment-based immigrants (and their family members accompanying or following to join under section 203(d) of such Act ( 8 U.S.C. 1153(d) )) whose immigrant worker petitions were filed no later than three years following the date of enactment of the Healthcare Workforce Resilience Act . (B) Reservations Of the visas authorized under subparagraph (A)\u2014 (i) 25,000 shall be reserved for professional nurses; and (ii) 15,000 shall be reserved for physicians. (C) Exemption from country caps Visas made available under this subsection\u2014 (i) shall not be subject to the per country numerical limitation set forth in section 202(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) ); and (ii) shall be issued in order of the priority date assigned at the time the visa petition was filed. (D) Additional limitation Visas may only be made available under this subsection to a beneficiary and such beneficiary's dependents if visas are not otherwise immediately available to such individuals pursuant to the worldwide and per country allocations set forth in sections 202(a)(2) and 203(b) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) and 1153(b)). (3) Number available (A) Unused visas Subject to subparagraph (B), the number calculated in this paragraph is the difference between\u2014 (i) the total number of employment-based visas that were made available in fiscal years 1992 through 2024; and (ii) the total number of such visas that were used in such fiscal years. (B) Reduction and limitation The number described in subparagraph (A) shall be reduced, for each fiscal year following the fiscal year during which the Healthcare Workforce Resilience Act is enacted, by the cumulative number of immigrant visas used pursuant to paragraph (1). (C) Family members (i) In general Family members described in section 203(d) of the Immigration and Nationality Act ( 8 U.S.C. 1153(d) ) who are accompanying or following to join a principal beneficiary seeking admission under this subsection shall be entitled to an unreserved visa in the same status and in the same order of consideration as such principal beneficiary. (ii) Exempt from skill-based numerical limitation Visas described in clause (i)\u2014 (I) shall be made available from the pool of recaptured unused immigrant visas calculated under subparagraph (A); and (II) shall not be counted against the total number of immigrant visas reserved for professional nurses and physicians under paragraph (2). (D) Rule of construction Nothing in this paragraph may be construed as affecting the application of section 201(c)(3)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1151(c)(3)(C) ). (4) Premium processing; expedited processing (A) Premium processing The Secretary of Homeland Security, in conjunction with the Secretary of State, shall provide premium processing procedures, as provided for under section 286(u) of the Immigration and Nationality Act ( 8 U.S.C. 1356(u) ), for reviewing and acting upon petitions and applications for immigrants described in paragraph (2). Notwithstanding such section, U.S. Citizenship and Immigration Services may not charge a premium fee for such services. (B) Shipping petitions The Director of U.S. Citizenship and Immigration Services shall expedite the shipping of each petition described in subparagraph (A) requiring consular processing to the Department of State immediately after\u2014 (i) the completed petition has been resolved; and (ii) the petitioner has replied to any request from U.S. Citizenship and Immigration Services for additional evidence. (C) Expedited processing The Secretary of State shall expedite the processing of applications for immigrants described in paragraph (2) after receiving a petition on behalf of such immigrants from U.S. Citizenship and Immigration Services. (5) Labor attestation Before an immigrant visa reserved under paragraph (2)(B)(i) is issued to an alien, the petitioner shall attest, in the job offer letter presented by the alien to a consular officer during the consular interview or to the Department of Homeland Security as an application for an adjustment of status, that the hiring of the alien has not displaced and will not displace a United States worker. .",
      "versionDate": "2025-09-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-09-10",
        "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S6539)"
      },
      "number": "2759",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthcare Workforce Resilience Act",
      "type": "S"
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
        "name": "Immigration",
        "updateDate": "2025-09-23T16:51:43Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5283ih.xml"
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
      "title": "Healthcare Workforce Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-18T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthcare Workforce Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-18T04:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance our Nation's nurse and physician workforce by recapturing unused immigrant visas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-18T04:18:17Z"
    }
  ]
}
```
