# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2759?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2759
- Title: Healthcare Workforce Resilience Act
- Congress: 119
- Bill type: S
- Bill number: 2759
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-01-20T23:17:43Z
- Update date including text: 2026-01-20T23:17:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S6539)
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S6539)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2759",
    "number": "2759",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Healthcare Workforce Resilience Act",
    "type": "S",
    "updateDate": "2026-01-20T23:17:43Z",
    "updateDateIncludingText": "2026-01-20T23:17:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S6539)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T19:33:59Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "ND"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "ME"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "DE"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "KS"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "IN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "CA"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "SD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "IL"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2759is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2759\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Durbin (for himself, Mr. Cramer , Mr. Welch , Ms. Collins , Mr. Coons , Mr. Marshall , Mr. Kelly , Mr. Young , Mr. Padilla , and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo enhance our Nation\u2019s nurse and physician workforce by recapturing unused immigrant visas.\n#### 1. Short title\nThis Act may be cited as the Healthcare Workforce Resilience Act .\n#### 2. Recapturing unused immigrant visas for professional nurses and physicians\nSection 106(d) of the American Competitiveness in the Twenty-first Century Act of 2000 (title I of Public Law 106\u2013313 ; 8 U.S.C. 1153 note) is amended to read as follows:\n(d) Recapture of unused employment-Based immigrant visas (1) In general Subject to paragraph (2), and notwithstanding any other provision of law, the number of employment-based visas made available under section 203(b) of the Immigration and Nationality Act ( 8 U.S.C. 1153(b) ) shall be increased by the number calculated under paragraph (3). (2) Limitations (A) In general Visas may only be made available under this subsection for up to 40,000 employment-based immigrants (and their family members accompanying or following to join under section 203(d) of such Act ( 8 U.S.C. 1153(d) )) whose immigrant worker petitions are filed not later than 3 years after the date of the enactment of the Healthcare Workforce Resilience Act . (B) Reservations Of the visas authorized under subparagraph (A)\u2014 (i) 25,000 shall be reserved for professional nurses; and (ii) 15,000 shall be reserved for physicians. (C) Exemption from country caps Visas made available under this subsection\u2014 (i) shall not be subject to the per country numerical limitation set forth in section 202(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) ); and (ii) shall be issued in order of the priority date assigned at the time the visa petition was filed. (D) Additional limitation Visas may only be made available under this subsection to a beneficiary and such beneficiary's dependents if visas are not otherwise immediately available to such individuals pursuant to the worldwide and per country allocations set forth in sections 202(a)(2) and 203(b) of the Immigration and Nationality Act ( 8 U.S.C. 1152(a)(2) and 1153(b)). (3) Number available (A) Unused visas Subject to subparagraph (B), the number calculated under this paragraph is the difference between\u2014 (i) the total number of employment-based visas that were made available for fiscal years 1992 through 2024; and (ii) the total number of such visas that were used in such fiscal years. (B) Reduction and limitation The number described in subparagraph (A) shall be reduced, for each fiscal year following the fiscal year during which the Healthcare Workforce Resilience Act is enacted, by the cumulative number of immigrant visas used pursuant to paragraph (1). (C) Family members (i) In general Family members described in section 203(d) of the Immigration and Nationality Act ( 8 U.S.C. 1153(d) ) who are accompanying or following to join a principal beneficiary seeking admission under this subsection shall be entitled to an unreserved visa in the same status and in the same order of consideration as such principal beneficiary. (ii) Exempt from skill-based numerical limitation Visas described in clause (i)\u2014 (I) shall be made available from the pool of recaptured unused immigrant visas calculated under subparagraph (A); and (II) shall not be counted against the total number of immigrant visas reserved for professional nurses and physicians under paragraph (2). (D) Rule of construction Nothing in this paragraph may be construed as affecting the application of section 201(c)(3)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1151(c)(3)(C) ). (4) Premium processing; expedited processing (A) Premium processing The Secretary of Homeland Security, in conjunction with the Secretary of State, shall provide premium processing procedures, as provided for under section 286(u) of the Immigration and Nationality Act ( 8 U.S.C. 1356(u) ), for reviewing and acting upon petitions and applications for immigrants described in paragraph (2). Notwithstanding such section, U.S. Citizenship and Immigration Services may not charge a premium fee for such services. (B) Shipping petitions The Director of U.S. Citizenship and Immigration Services shall expedite the shipping of each petition described in subparagraph (A) requiring consular processing to the Department of State immediately after\u2014 (i) the completed petition has been resolved; and (ii) the petitioner has replied to any request from U.S. Citizenship and Immigration Services for additional evidence. (C) Expedited processing The Secretary of State shall expedite the processing of applications for immigrants described in paragraph (2) after receiving a petition on behalf of such immigrants from U.S. Citizenship and Immigration Services. (5) Labor attestation Before an immigrant visa reserved under paragraph (2)(B)(i) is issued to an alien, the petitioner shall attest, in the job offer letter presented by the alien to a consular officer during the consular interview or to the Department of Homeland Security as an application for an adjustment of status, that the hiring of the alien has not displaced and will not displace a United States worker. .",
      "versionDate": "2025-09-10",
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
        "actionDate": "2025-09-10",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "5283",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Healthcare Workforce Resilience Act",
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
        "name": "Immigration",
        "updateDate": "2025-09-23T16:51:28Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2759is.xml"
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
      "title": "Healthcare Workforce Resilience Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T12:03:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Healthcare Workforce Resilience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance our Nation's nurse and physician workforce by recapturing unused immigrant visas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:23Z"
    }
  ]
}
```
