# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4236
- Title: FADS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4236
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-07-29T21:46:54Z
- Update date including text: 2025-07-29T21:46:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-06-27: Introduced in House

## Actions

- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4236",
    "number": "4236",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FADS Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-29T21:46:54Z",
    "updateDateIncludingText": "2025-07-29T21:46:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-27",
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
          "date": "2025-06-27T13:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "NE"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "FL"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4236ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4236\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Mills (for himself, Mr. Fleischmann , Mr. Bacon , and Mr. Steube ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo clarify the authority of the Department of Energy to dispose of certain foreign-origin fissile or radiological materials at the Waste Isolation Pilot Plant.\n#### 1. Short title\nThis Act may be cited as the Foreign Americium Disposal and Storage Act of 2025 or the FADS Act of 2025 .\n#### 2. Clarification of authority to dispose of certain fissile or radiological materials\n##### (a) Findings\nCongress finds the following:\n**(1)**\nWhile United States-origin americium-241 (Am\u2013241) sealed sources recovered by the National Nuclear Security Administration of the Department of Energy may be disposed of at the Waste Isolation Pilot Plant (WIPP), Russian-origin Am\u2013241 sources may not be.\n**(2)**\nSection 2(19) of the WIPP Land Withdrawal Act of 1991 identifies WIPP as the location for the disposal of radioactive waste materials generated by atomic energy defense activities .\n**(3)**\nThe Am\u2013241 sources of concern that may not currently be eligible for disposal at WIPP have the same isotopic properties and are often colocated with sources that are eligible for disposal at WIPP.\n**(4)**\nRussian-origin sealed sources, once confirmed to meet the WIPP Waste Acceptance Criteria, should be eligible for disposal at WIPP.\n**(5)**\nThe Carlsbad Field Office of the Department estimates the volume to be disposed is equivalent to 1 to 2 shipments a year and will have a negligible impact on WIPP operations.\n**(6)**\nThe Department, the Nuclear Regulatory Commission (NRC), and the international community have identified Am\u2013241 as a radioisotope that should be protected due to the possibility of its use in a radiological dispersal device.\n**(7)**\nAs part of its defense nuclear nonproliferation mission, the National Nuclear Security Administration recovers thousands of disused sealed sources from domestic and international facilities.\n**(8)**\nCodifying a disposition pathway for these Am\u2013241 sources will allow the National Nuclear Security Administration to accelerate their removal and reduce the availability of material that could be used in a dirty bomb.\n##### (b) Clarification\nSection 3132(c)(1) of the Ronald W. Reagan National Defense Authorization Act for Fiscal Year 2005 ( 50 U.S.C. 2569(c)(1) ) is amended by adding at the end the following new subparagraph:\n(N) (i) The collection, storage, and safe disposal of the materials described in clause (ii) as waste materials generated by atomic energy defense activities for the purpose of disposal of such materials at WIPP (as defined in section 2(19) of the Waste Isolation Pilot Plant Land Withdrawal Act ( Public Law 102\u2013579 ; 106 Stat. 4777)). (ii) The materials described in this clause are proliferation-attractive fissile materials or radiological materials that\u2014 (I) contain transuranic elements of foreign-origin; and (II) but for subclause (I), are similar to proliferation-attractive fissile materials or radiological materials covered by this section. .",
      "versionDate": "2025-06-27",
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
        "name": "International Affairs",
        "updateDate": "2025-07-29T21:46:54Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4236ih.xml"
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
      "title": "FADS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FADS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Americium Disposal and Storage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify the authority of the Department of Energy to dispose of certain foreign-origin fissile or radiological materials at the Waste Isolation Pilot Plant.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T07:18:31Z"
    }
  ]
}
```
