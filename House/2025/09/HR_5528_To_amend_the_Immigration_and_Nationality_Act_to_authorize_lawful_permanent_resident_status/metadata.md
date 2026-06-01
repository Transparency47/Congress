# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5528
- Title: America’s CHILDREN Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5528
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-02-24T09:05:47Z
- Update date including text: 2026-02-24T09:05:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5528",
    "number": "5528",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "R000305",
        "district": "2",
        "firstName": "Deborah",
        "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
        "lastName": "Ross",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "America\u2019s CHILDREN Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:47Z",
    "updateDateIncludingText": "2026-02-24T09:05:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:03:05Z",
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
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
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
      "sponsorshipDate": "2025-09-19",
      "state": "GA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "NE"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "AZ"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "IA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MI"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "AZ"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5528ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5528\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Ms. Ross (for herself, Mrs. Miller-Meeks , Mr. Krishnamoorthi , Ms. Salazar , Mr. Bera , Mr. Fitzpatrick , Mr. Johnson of Georgia , Mr. Bacon , Ms. Houlahan , Mr. Obernolte , Ms. Jayapal , Mr. Rutherford , Mr. Peters , Mr. Ciscomani , Ms. Scanlon , Mr. Nunn of Iowa , Ms. DelBene , Mr. Thanedar , Mr. Stanton , and Mr. Min ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Immigration and Nationality Act to authorize lawful permanent resident status for certain college graduates who entered the United States as children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the America\u2019s CHILDREN Act of 2025 or the Protecting Children of Long-Term Visa Holders Act of 2025 .\n#### 2. Permanent resident status for certain college graduates who entered the United States as children\n##### (a) Requirements\nSection 201(b)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1151(b)(1) ) is amended by adding at the end the following:\n(F) Any alien who\u2014 (i) is not inadmissible under section 212(a) or deportable under section 237(a); (ii) was lawfully present in the United States as a dependent child of a nonimmigrant admitted to engage in employment in the United States (other than a nonimmigrant described in subparagraph (A), (G), (N), or (S) of section 101(a)(15)) for an aggregate period of not less than 8 years; (iii) on the date on which an application under section 204(a)(1)(M) is submitted, has been lawfully present in the United States for an aggregate period of not less than 10 years; and (iv) has graduated from an institution of higher education (as defined in section 102(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(a) )) in the United States. .\n##### (b) Petition\nSection 204(a)(1) of the Immigration and Nationality Act ( 8 U.S.C. 1154(a)(1) ) is amended by adding at the end the following:\n(M) Any alien entitled to classification under section 201(b)(1)(F) may file a petition with the Secretary of Homeland Security for such classification. .\n#### 3. Age-out protections and priority date retention\n##### (a) Age-Out protections\n**(1) In general**\nThe Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ) is amended\u2014\n**(A)**\nin section 101(b) ( 8 U.S.C. 1101(b) ), by adding at the end the following:\n(6) Determination of child status A determination as to whether an alien is a child shall be made as follows: (A) In general For purposes of a petition under section 204 and any subsequent application for an immigrant visa or adjustment of status, such determination shall be made using the age of the alien on the earlier of\u2014 (i) the date on which the petition is filed with the Secretary of Homeland Security; or (ii) the date on which an application for a labor certification under section 212(a)(5)(A)(i) is filed with the Secretary of Labor. (B) Certain dependents of nonimmigrants With respect to an alien who, for an aggregate period of 8 years before attaining the age of 21, was in the status of a dependent child of a nonimmigrant pursuant to a lawful admission as an alien eligible to be employed in the United States (other than a nonimmigrant described in subparagraph (A), (G), (N), or (S) of section 101(a)(15)), notwithstanding clause (i), the determination of the alien\u2019s age shall be based on the date on which such initial nonimmigrant employment-based petition or application was filed by the alien's nonimmigrant parent. (C) Failure to acquire status as alien lawfully admitted for permanent residence With respect to an alien who has not sought to acquire status as an alien lawfully admitted for permanent residence during the 2 years beginning on the date on which an immigrant visa becomes available to such alien, the alien\u2019s age shall be determined based on the alien's biological age, unless the failure to seek to acquire such status was due to extraordinary circumstances. ; and\n**(B)**\nin section 201(f) ( 8 U.S.C. 1151 )\u2014\n**(i)**\nby striking the subsection heading and all that follows through termination date.\u2014 in paragraph (3) and inserting Rule for determining whether certain aliens are immediate relatives.\u2014 ; and\n**(ii)**\nby striking paragraph (4).\n**(2) Effective date**\n**(A) In general**\nThe amendments made by this subsection shall be effective as if included in the Child Status Protection Act ( Public Law 107\u2013208 ; 116 Stat. 927).\n**(B) Motion to reopen or reconsider**\n**(i) In general**\nA motion to reopen or reconsider the denial of a petition or application described in the amendment made by paragraph (1)(A) may be granted if\u2014\n**(I)**\nsuch petition or application would have been approved if the amendment described in such paragraph had been in effect at the time of adjudication of the petition or application;\n**(II)**\nthe individual seeking relief pursuant to such motion was in the United States at the time the underlying petition or application was filed; and\n**(III)**\nsuch motion is filed with the Secretary of Homeland Security or the Attorney General not later than the date that is 2 years after the date of the enactment of this Act.\n**(ii) Exemption from numerical limitations**\nNotwithstanding any other provision of law, an individual granted relief pursuant to a motion to reopen or reconsider under clause (i) shall be exempt from the numerical limitations in sections 201, 202, and 203 of the Immigration and Nationality Act ( 8 U.S.C. 1151 , 1152, and 1153).\n##### (b) Nonimmigrant dependent children\nSection 214 of the Immigration and Nationality Act ( 8 U.S.C. 1184 ) is amended by adding at the end the following:\n(s) Derivative beneficiaries (1) In general Except as described in paragraph (2), the determination as to whether an alien who is the derivative beneficiary of a properly filed pending or approved immigrant petition under section 204 is eligible to be a dependent child shall be based on whether the alien is determined to be a child under section 101(b)(6). (2) Long-term dependents If otherwise eligible, an alien who is determined to be a child pursuant to section 101(b)(6)(B) may change status to, or extend status as, a dependent child of a nonimmigrant with an approved employment-based petition under this section or an approved application under section 101(a)(15)(E), notwithstanding such alien\u2019s marital status. (3) Employment authorization An alien admitted to the United States as a dependent child of a nonimmigrant who is described in this section is authorized to engage in employment in the United States incident to status. .\n##### (c) Priority date retention\nSection 203(h) of the Immigration and Nationality Act ( 8 U.S.C. 1153(h) ) is amended\u2014\n**(1)**\nby striking the subsection heading and inserting Retention of priority dates ;\n**(2)**\nby striking paragraphs (1) through (4);\n**(3)**\nby redesignating paragraph (5) as paragraph (3); and\n**(4)**\nby inserting before paragraph (3) the following:\n(1) In general The priority date for an individual shall be the date on which a petition under section 204 is filed with the Secretary of Homeland Security or the Secretary of State, as applicable, unless such petition was preceded by the filing of a labor certification with the Secretary of Labor, in which case the date on which the labor certification is filed shall be the priority date. (2) Applicability The principal beneficiary and all derivative beneficiaries shall retain the priority date associated with the earliest of any approved petition or labor certification, and such priority date shall be applicable to any subsequently approved petition. .",
      "versionDate": "2025-09-19",
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
        "actionDate": "2025-09-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2886",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "America\u2019s CHILDREN Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on the Judiciary, and in addition to the Committees on Homeland Security, Ways and Means, Transportation and Infrastructure, Education and Workforce, Oversight and Government Reform, and Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DIGNIDAD (Dignity) Act of 2025",
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
        "updateDate": "2025-11-18T18:30:32Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5528ih.xml"
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
      "title": "America\u2019s CHILDREN Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Children of Long-Term Visa Holders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "America\u2019s CHILDREN Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Immigration and Nationality Act to authorize lawful permanent resident status for certain college graduates who entered the United States as children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:18Z"
    }
  ]
}
```
