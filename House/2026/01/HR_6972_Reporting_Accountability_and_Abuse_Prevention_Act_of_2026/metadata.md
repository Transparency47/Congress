# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6972
- Title: Reporting Accountability and Abuse Prevention Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 6972
- Origin chamber: House
- Introduced date: 2026-01-07
- Update date: 2026-02-11T09:06:11Z
- Update date including text: 2026-02-11T09:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-07: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-01-07: Introduced in House

## Actions

- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Introduced in House
- 2026-01-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-07",
    "latestAction": {
      "actionDate": "2026-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6972",
    "number": "6972",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Reporting Accountability and Abuse Prevention Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-11T09:06:11Z",
    "updateDateIncludingText": "2026-02-11T09:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-07",
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
          "date": "2026-01-07T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "SC"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "LA"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "AZ"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "PA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "IL"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "VA"
    },
    {
      "bioguideId": "C001115",
      "district": "27",
      "firstName": "Michael",
      "fullName": "Rep. Cloud, Michael [R-TX-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Cloud",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "W000798",
      "district": "5",
      "firstName": "Tim",
      "fullName": "Rep. Walberg, Tim [R-MI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Walberg",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "IN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "NC"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-01-21",
      "state": "IL"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "AZ"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6972ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6972\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2026 Mr. Smucker (for himself, Mrs. Biggs of South Carolina , Mr. Gill of Texas , Mr. Higgins of Louisiana , Mr. Gosar , Ms. Tenney , Mr. Joyce of Pennsylvania , Mr. Bost , Mr. Weber of Texas , and Mr. Rose ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title X of the Public Health Service Act to require grant recipients to comply with all applicable State and local laws requiring notification or reporting of child abuse, child molestation, sexual abuse, rape, incest, intimate partner violence, or human trafficking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reporting Accountability and Abuse Prevention Act of 2026 .\n#### 2. Compliance by projects funded under title X with State and local sexual abuse reporting requirements\nTitle X of the Public Health Service Act ( 42 U.S.C. 300 et seq. ) is amending by adding at the end the following:\n1009. Compliance with State and local sexual abuse reporting requirements (a) In general As a condition on the award or renewal of a grant under this title for any project or program, the Secretary shall require the grant recipient to comply with all applicable State and local laws requiring notification or reporting of child abuse, child molestation, sexual abuse, rape, incest, intimate partner violence, or human trafficking (in this section referred to as State notification laws ). (b) Required compliance In ensuring compliance with subsection (a) for a project or program, the grant recipient shall provide to the Secretary appropriate documentation or otherwise demonstrate to the Secretary\u2019s satisfaction that the grant recipient\u2014 (1) has in place and implements a plan to comply with State notification laws, including, at a minimum, policies and procedures that include\u2014 (A) a summary of obligations under State notification laws of the project or program, or of each organization and individual carrying out the project or program, including any obligation to inquire about or determine the age of a minor patient or of a minor patient\u2019s sexual partner; (B) timely and adequate annual training of all individuals (whether or not they are employees) serving patients for, or on behalf of, the project or program regarding\u2014 (i) compliance with State notification laws; (ii) policies and procedures of the project or program with respect to notification and reporting of child abuse, child molestation, sexual abuse, rape, incest, intimate partner violence, and human trafficking; and (iii) appropriate interventions, strategies, and referrals to improve the safety and current situation of the patient; (C) protocols to ensure that every minor who presents for treatment is provided counseling on how to resist attempts to coerce the minor into engaging in sexual activities; and (D) a commitment to conduct a preliminary screening of any minor who presents with a sexually transmitted disease, pregnancy, or any suspicion of abuse, in order to rule out victimization of the minor; and (2) maintains records that demonstrate compliance with each of the requirements set forth in paragraph (1) and\u2014 (A) indicate the age of minor patients; (B) document each notification or report made pursuant to State notification laws; and (C) indicate the age of the minor patient\u2019s sexual partners if such age is an element of a State notification law under which a report is required. (c) Review of records As a condition on the award or renewal of a grant under this title for any project or program, a grant recipient shall agree to allow the Secretary, the Inspector General of the Department of Health and Human Services, and the Comptroller General of the United States to review the records maintained by the grant recipient, including any contractor or subgrantee of the grant recipient, for the purpose of ensuring compliance with this section. (d) Penalties for noncompliance The Secretary shall\u2014 (1) if the Secretary finds that a grantee under this title has violated subsection (a), (b), or (c), work with the grantee to remedy such noncompliance; and (2) if the Secretary finds that the grantee commits a subsequent violation of subsection (a), (b), or (c)\u2014 (A) seek repayment of all monetary Federal assistance received by the grantee under this title on or after the date of enactment of the Reporting Accountability and Abuse Prevention Act of 2026 ; and (B) not award or provide any assistance under this title to the grantee for a period of at least 36 months following the date of finding that the grantee has committed such subsequent violation. .",
      "versionDate": "2026-01-07",
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
        "name": "Health",
        "updateDate": "2026-01-26T14:52:09Z"
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
      "date": "2026-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6972ih.xml"
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
      "title": "Reporting Accountability and Abuse Prevention Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reporting Accountability and Abuse Prevention Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title X of the Public Health Service Act to require grant recipients to comply with all applicable State and local laws requiring notification or reporting of child abuse, child molestation, sexual abuse, rape, incest, intimate partner violence, or human trafficking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:55Z"
    }
  ]
}
```
