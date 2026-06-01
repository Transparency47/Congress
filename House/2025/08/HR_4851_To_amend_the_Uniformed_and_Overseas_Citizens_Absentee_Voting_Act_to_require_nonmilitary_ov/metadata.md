# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4851?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4851
- Title: PROVE Act
- Congress: 119
- Bill type: HR
- Bill number: 4851
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2025-09-15T18:07:54Z
- Update date including text: 2025-09-15T18:07:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4851",
    "number": "4851",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "PROVE Act",
    "type": "HR",
    "updateDate": "2025-09-15T18:07:54Z",
    "updateDateIncludingText": "2025-09-15T18:07:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:07:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TN"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "AZ"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4851ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4851\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Hamadeh of Arizona (for himself, Mr. Burchett , and Mr. Ogles ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Uniformed and Overseas Citizens Absentee Voting Act to require nonmilitary overseas voters to provide evidence of residence in a State as a condition of receiving an absentee ballot under such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Proving Residency for Overseas Voter Eligibility Act or the PROVE Act .\n#### 2. Requiring evidence of recent residence in State for nonmilitary overseas voters\n##### (a) Requirement\nThe Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20301 et seq. ) is amended by inserting after section 104 the following new section:\n104A. Requiring evidence of recent residence in State for nonmilitary overseas voters (a) Requirement (1) Absentee ballots transmitted by State A State may not transmit an absentee ballot to an overseas voter unless the voter provides the State with a verifiable mailing address within the State of\u2014 (A) a current residence of the voter; or (B) a current residence of a spouse, parent, or legal guardian of the voter. (2) Federal write-in absentee ballot The Presidential designee may not transmit a Federal write-in absentee ballot to an overseas voter under section 103 unless the voter provides the Presidential designee with a verifiable mailing address within the State in which the voter seeks to vote of\u2014 (A) a current residence of the voter; or (B) a current residence of a spouse, parent, or legal guardian of the voter. (b) Voting in elections for Federal office in District of Columbia An overseas voter who fails to provide the information required under subsection (a) for the receipt of an absentee ballot in a regularly scheduled general election for Federal office held in the State in which the voter seeks to vote\u2014 (1) may vote in a regularly scheduled general election for Federal office in the District of Columbia which is held on the same date; and (2) for purposes of this Act and the applicable laws of the District of Columbia governing elections for Federal office in the District of Columbia, shall be considered to be a resident of the District of Columbia with respect to that election. (c) Non-Application to absent uniformed services voter This section does not apply to an absent uniformed services voter. .\n##### (b) Effective date\nThis Act and the amendments made by this Act shall apply with respect to elections held during 2026 or any succeeding year.",
      "versionDate": "2025-08-01",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-15T18:07:54Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4851ih.xml"
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
      "title": "PROVE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PROVE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proving Residency for Overseas Voter Eligibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Uniformed and Overseas Citizens Absentee Voting Act to require nonmilitary overseas voters to provide evidence of residence in a State as a condition of receiving an absentee ballot under such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:32Z"
    }
  ]
}
```
