# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/250?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/250
- Title: To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.
- Congress: 119
- Bill type: HR
- Bill number: 250
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-05-30T23:51:43Z
- Update date including text: 2025-05-30T23:51:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-26 15:31:09 - Floor: Mr. Steil moved to suspend the rules and pass the bill.
- 2025-02-26 15:31:11 - Floor: Considered under suspension of the rules. (consideration: CR H854-855)
- 2025-02-26 15:31:12 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 250.
- 2025-02-26 15:43:41 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)
- 2025-02-26 15:43:41 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)
- 2025-02-26 15:43:42 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-27 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-26 15:31:09 - Floor: Mr. Steil moved to suspend the rules and pass the bill.
- 2025-02-26 15:31:11 - Floor: Considered under suspension of the rules. (consideration: CR H854-855)
- 2025-02-26 15:31:12 - Floor: DEBATE - The House proceeded with forty minutes of debate on H.R. 250.
- 2025-02-26 15:43:41 - Floor: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)
- 2025-02-26 15:43:41 - Floor: Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)
- 2025-02-26 15:43:42 - Floor: Motion to reconsider laid on the table Agreed to without objection.
- 2025-02-27 - IntroReferral: Received in the Senate and Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/250",
    "number": "250",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.",
    "type": "HR",
    "updateDate": "2025-05-30T23:51:43Z",
    "updateDateIncludingText": "2025-05-30T23:51:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Received in the Senate and Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H38310",
      "actionDate": "2025-02-26",
      "actionTime": "15:43:42",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Motion to reconsider laid on the table Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H37300",
      "actionDate": "2025-02-26",
      "actionTime": "15:43:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2025-02-26",
      "actionTime": "15:43:41",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in House: On motion to suspend the rules and pass the bill Agreed to by voice vote. (text: CR H854)",
      "type": "Floor"
    },
    {
      "actionCode": "H8D000",
      "actionDate": "2025-02-26",
      "actionTime": "15:31:12",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "DEBATE - The House proceeded with forty minutes of debate on H.R. 250.",
      "type": "Floor"
    },
    {
      "actionCode": "H30000",
      "actionDate": "2025-02-26",
      "actionTime": "15:31:11",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Considered under suspension of the rules. (consideration: CR H854-855)",
      "type": "Floor"
    },
    {
      "actionCode": "H30300",
      "actionDate": "2025-02-26",
      "actionTime": "15:31:09",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Mr. Steil moved to suspend the rules and pass the bill.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-02-27T17:08:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:31:50Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NJ"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MO"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "NV"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "NY"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "FL"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "NE"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "DE"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "AR"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "TN"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "PA"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "IL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "PA"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 250\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Ms. Houlahan (for herself, Mr. Fitzpatrick , Mrs. McClain , Mr. Moulton , Mr. Meuser , Mrs. Watson Coleman , Mr. Joyce of Pennsylvania , Mrs. Kiggans of Virginia , Mr. Cleaver , Ms. Malliotakis , Mrs. Dingell , Mr. Khanna , Mr. Evans of Pennsylvania , Ms. Dean of Pennsylvania , Ms. Titus , Mr. Lawler , Mr. Thompson of Pennsylvania , Ms. Lee of Florida , and Mrs. Bice ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.\n#### 1. Procurement and placement of statue of Benjamin Franklin in the United States Capitol\n##### (a) Obtaining of statue\nNot later than December 31, 2025, the Joint Committee on the Library shall enter into an agreement to obtain a statue of Benjamin Franklin, under such terms and conditions as the Joint Committee considers appropriate consistent with applicable law.\n##### (b) Placement\nNot later than December 31, 2026, the Joint Committee shall place the statue obtained under subsection (a) in a suitable permanent location in the United States Capitol where the statue is accessible to the public during a guided tour of the Capitol provided by the Capitol Visitor Center.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250rfs.xml",
      "text": "IIB\n119th CONGRESS\n1st Session\nH. R. 250\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Received; read twice and referred to the Committee on Rules and Administration\nAN ACT\nTo direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.\n#### 1. Procurement and placement of statue of Benjamin Franklin in the United States Capitol\n##### (a) Obtaining of statue\nNot later than December 31, 2025, the Joint Committee on the Library shall enter into an agreement to obtain a statue of Benjamin Franklin, under such terms and conditions as the Joint Committee considers appropriate consistent with applicable law.\n##### (b) Placement\nNot later than December 31, 2026, the Joint Committee shall place the statue obtained under subsection (a) in a suitable permanent location in the United States Capitol where the statue is accessible to the public during a guided tour of the Capitol provided by the Capitol Visitor Center.",
      "versionDate": "2025-02-27",
      "versionType": "Referred in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250eh.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 250\nIN THE HOUSE OF REPRESENTATIVES\nAN ACT\nTo direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.\n#### 1. Procurement and placement of statue of Benjamin Franklin in the United States Capitol\n##### (a) Obtaining of statue\nNot later than December 31, 2025, the Joint Committee on the Library shall enter into an agreement to obtain a statue of Benjamin Franklin, under such terms and conditions as the Joint Committee considers appropriate consistent with applicable law.\n##### (b) Placement\nNot later than December 31, 2026, the Joint Committee shall place the statue obtained under subsection (a) in a suitable permanent location in the United States Capitol where the statue is accessible to the public during a guided tour of the Capitol provided by the Capitol Visitor Center.",
      "versionDate": "",
      "versionType": "Engrossed in House"
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
        "actionDate": "2025-01-09",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "44",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Joint Committee on the Library",
            "updateDate": "2025-02-24T19:54:01Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-02-24T19:54:01Z"
          },
          {
            "name": "U.S. Capitol",
            "updateDate": "2025-02-24T19:54:01Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-02-24T19:54:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-07T12:50:11Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
    "originChamber": "House",
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
          "measure-id": "id119hr250",
          "measure-number": "250",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr250v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>"
        },
        "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr250.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr250"
    },
    "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr250"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250rfs.xml"
        }
      ],
      "type": "Referred in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr250eh.xml"
        }
      ],
      "type": "Engrossed in House"
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
      "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T01:03:28Z"
    },
    {
      "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T09:05:30Z"
    }
  ]
}
```
