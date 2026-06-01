# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8028?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8028
- Title: SNAP Fraud Reporting Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8028
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-05-20T08:08:19Z
- Update date including text: 2026-05-20T08:08:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8028",
    "number": "8028",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David J. [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "SNAP Fraud Reporting Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:19Z",
    "updateDateIncludingText": "2026-05-20T08:08:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "CO"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "AL"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "SC"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "WI"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "NC"
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
      "sponsorshipDate": "2026-03-19",
      "state": "AZ"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "SC"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "SC"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "MI"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "SD"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-27",
      "state": "PA"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "TN"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "SC"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "GA"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8028ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8028\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Taylor (for himself, Ms. Boebert , Mr. Moore of Alabama , Ms. Mace , Mr. Wied , Mr. Hunt , Mr. Harris of North Carolina , Mr. Gosar , Mr. Timmons , Mr. Fry , and Mr. Barrett ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require States to provide data on fraud within the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008.\n#### 1. Short title\nThis Act may be cited as the SNAP Fraud Reporting Act of 2026 .\n#### 2. Required State submission of SNAP fraud data\n##### (a) Initial submission of data\nNot later than 180 days after the date of the enactment of this Act, each State shall submit to the Secretary of Agriculture data on fraud that occurred in the supplemental nutrition assistance program for the then most recently concluded 5 fiscal years available. Such data shall include the following:\n**(1)**\nThe number of supplemental nutrition assistance program fraud cases open for investigation.\n**(2)**\nThe total number of fraud cases identified, including substantiated fraud committed by criminals such as card skimming and card cloning, and the total dollar amount of fraud cases identified.\n**(3)**\nThe number and type of enforcement actions taken against supplemental nutrition assistance program fraud.\n**(4)**\nThe amount of the recoveries in such cases.\n**(5)**\nFor each fiscal year that begins after the after the enactment of this Act, all data on the number of people disqualified for fraud which were found to be deceased people or using a deceased person's identity who received supplemental nutrition assistance program benefits during each fiscal year and the dollar amount of benefits issued.\n**(6)**\nFor each fiscal year that begins after the after the enactment of this Act, all data on the number of people disqualified for fraud which were found to have submitted no social security number or used falsified, recycled, stolen, or purchased social security numbers during each fiscal year and the dollar amount of such benefits.\n##### (b) Subsequent submission of data\nNot later than 60 days after October 1, 2028, and not later than 60 days after each October 1 thereafter, each State shall submit to the Secretary of Agriculture data of the kind described in subsection (a) on fraud that occurred in the supplemental nutrition assistance program for the then most recently concluded fiscal year.\n##### (c) Penalty\nIf a State does not provide the requested data required by this section not later than the applicable date, the Secretary shall withhold supplemental nutrition assistance program administrative funds from such State until such data are received from such State.\n#### 3. Reports to the Congress\n##### (a) Initial report\nNot later than 180 days after receiving all of the data required to be submitted under section 2(a) by States, the Secretary shall\u2014\n**(1)**\nsubmit to the Congress a report that contains the findings of the Secretary, and\n**(2)**\nshall publish such report online.\n##### (b) Subsequent reports\nNot later than 180 days after October 1, 2028, and not later than 180 days after each October 1 thereafter, after receiving all of the data required to be submitted under section 2(b) by States for the fiscal year involved, Secretary shall\u2014\n**(1)**\nsubmit a report of the kind described in subsection (a) based on such data for the most recently concluded fiscal year, and\n**(2)**\npublish such report online.",
      "versionDate": "2026-03-19",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-09T14:22:46Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8028ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SNAP Fraud Reporting Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-06T16:38:26Z"
    },
    {
      "title": "SNAP Fraud Reporting Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-06T16:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require States to provide data on fraud within the supplemental nutrition assistance program established under the Food and Nutrition Act of 2008.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-06T16:33:30Z"
    }
  ]
}
```
