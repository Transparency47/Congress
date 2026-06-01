# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5409
- Title: Territory Health Revitalization Act
- Congress: 119
- Bill type: HR
- Bill number: 5409
- Origin chamber: House
- Introduced date: 2025-09-16
- Update date: 2026-04-06T20:27:24Z
- Update date including text: 2026-04-06T20:27:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-16: Introduced in House

## Actions

- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Introduced in House
- 2025-09-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5409",
    "number": "5409",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000610",
        "district": "",
        "firstName": "Stacey",
        "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
        "lastName": "Plaskett",
        "party": "D",
        "state": "VI"
      }
    ],
    "title": "Territory Health Revitalization Act",
    "type": "HR",
    "updateDate": "2026-04-06T20:27:24Z",
    "updateDateIncludingText": "2026-04-06T20:27:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-16",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T14:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "GU"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "AS"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MP"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "PR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5409ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5409\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 16, 2025 Ms. Plaskett (for herself, Mr. Moylan , Mrs. Radewagen , Ms. King-Hinds , and Mr. Hern\u00e1ndez ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide a set-aside of funds for the territories under the health profession opportunity grant program under section 2008 of the Social Security Act, to make the Commonwealth of the Northern Mariana Islands eligible for the grants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Territory Health Revitalization Act .\n#### 2. Set-aside for the territories\nSection 2008(c)(1) of the Social Security Act ( 42 U.S.C. 1397g(c)(1) ) is amended by inserting 5 percent of which for each fiscal year shall be reserved for grants to States other than the 50 States and the District of Columbia before the period.\n#### 3. Eligibility of the Commonwealth of the Northern Mariana Islands\nSection 2008(a)(4) of the Social Security Act ( 42 U.S.C. 1397g(a)(4) ) is amended by striking subparagraph (E).\n#### 4. Guarantee of grantees in the territories\nSection 2008(a)(2) of the Social Security Act ( 42 U.S.C. 1397g(a)(2) ) is amended by adding at the end the following:\n(D) Guarantee of grantees in the territories The Secretary shall award at least 2 grants under this subsection to an eligible entity that is located in a territory, to the extent there are a sufficient number applications submitted by such an eligible entity that meet the requirements of subparagraph (B). .\n#### 5. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025.",
      "versionDate": "2025-09-16",
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
        "updateDate": "2026-04-06T20:27:24Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5409ih.xml"
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
      "title": "Territory Health Revitalization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Territory Health Revitalization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide a set-aside of funds for the territories under the health profession opportunity grant program under section 2008 of the Social Security Act, to make the Commonwealth of the Northern Mariana Islands eligible for the grants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T04:18:19Z"
    }
  ]
}
```
