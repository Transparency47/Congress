# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1581
- Title: Fort Monroe National Historical Park Establishment Act
- Congress: 119
- Bill type: HR
- Bill number: 1581
- Origin chamber: House
- Introduced date: 2025-02-25
- Update date: 2026-02-06T19:34:06Z
- Update date including text: 2026-02-06T19:34:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-02-25: Introduced in House

## Actions

- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Introduced in House
- 2025-02-25 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1581",
    "number": "1581",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "S000185",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
        "lastName": "Scott",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Fort Monroe National Historical Park Establishment Act",
    "type": "HR",
    "updateDate": "2026-02-06T19:34:06Z",
    "updateDateIncludingText": "2026-02-06T19:34:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
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
      "sponsorshipDate": "2025-02-25",
      "state": "VA"
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
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "VA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1581ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1581\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 25, 2025 Mr. Scott of Virginia (for himself, Mr. Wittman , Ms. McClellan , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo establish the Fort Monroe National Historical Park in the Commonwealth of Virginia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fort Monroe National Historical Park Establishment Act .\n#### 2. Definitions\nIn this Act:\n**(1) Commonwealth**\nThe term Commonwealth means the Commonwealth of Virginia.\n**(2) Map**\nThe term Map means the map titled Fort Monroe National Historical Park Proposed Boundary , numbered 250/193734, and dated June 2024.\n**(3) Historical park**\nThe term Historical Park means the Fort Monroe National Historical Park established by section (3)(a).\n**(4) Secretary**\nThe term Secretary means the Secretary of the Interior.\n#### 3. Establishment of Fort Monroe National Historical Park\n##### (a) In general\nThere is established the Fort Monroe National Historical Park in the Commonwealth to preserve the historic, natural, and recreational resources of Fort Monroe and interpret for the benefit of present and future generations\u2014\n**(1)**\nOld Point Comfort, its relationship to the voyages of Captain John Smith, its location as the first entry place of captive Africans into English North America, its use for successive fortifications, and its role in the War of 1812;\n**(2)**\nthe development and use of Fort Monroe as a coastal defense facility and artillery training center, including its military and community life;\n**(3)**\nthe fort\u2019s role in the Civil War, including the 1861 Contraband Decision providing a pathway to freedom for those escaping enslavement during that war, and the formation and service of United States Colored Troop units stationed at Fort Monroe;\n**(4)**\npersons and events associated with the fort, which contributed to its and the Nation\u2019s history, and their relevance to modern society; and\n**(5)**\nthe natural and recreational resource values associated with Fort Monroe.\n##### (b) Abolishment of national monument\nThe Fort Monroe National Monument, established by Presidential Proclamation 8750 of November 1, 2011 ( 54 U.S.C. 320301 note), is abolished and all land or interests in land therein are incorporated into, and shall be considered to be part of, the Historical Park.\n##### (c) Availability of funds\nAny unobligated funds available for purposes of the Fort Monroe National Monument shall be available for purposes of the Historical Park.\n##### (d) References\nAny reference in a law, regulation, document, record, map, or other paper of the United States to Fort Monroe National Monument shall be deemed to be a reference to Fort Monroe National Historical Park .\n#### 4. Boundary; Acquisition of land\n##### (a) Boundary\nThe boundary of the Historical Park shall be as generally depicted on the Map.\n##### (b) Availability of Map\nThe Map shall be on file and available for public inspection in the appropriate offices of the National Park Service.\n##### (c) Acquisition of land\nThe Secretary may acquire land, including interests in land, within the boundaries of the Historical Park by donation, transfer, exchange, or purchase from a willing seller using donated or appropriated funds.\n#### 5. Administration\n##### (a) In general\nThe Secretary shall administer the Historical Park in accordance with\u2014\n**(1)**\nthis Act; and\n**(2)**\nthe laws generally applicable to units of the National Park System, including\u2014\n**(A)**\nsection 100101(a), chapter 1003, and sections 100751(a), 100752, 100753 and 102101 of title 54, United States Code; and\n**(B)**\nchapter 3201 of title 54, United States Code.\n##### (b) Federal, commonwealth, and local jurisdiction\n**(1) Federal authority**\nExcept as otherwise provided in this Act, nothing shall enlarge, diminish or modify any authority of the United States to carry out Federal laws and regulations on Federal land located within the boundary of the Historical Park.\n**(2) Commonwealth authority**\nNothing in this Act enlarges, diminishes, or modifies any authority of the Commonwealth, or any political subdivision of the Commonwealth\u2014\n**(A)**\nto exercise civil and criminal jurisdiction unless an agreement for concurrent jurisdiction is executed and modifies Commonwealth or local government jurisdiction in any way; or\n**(B)**\nto carry out Commonwealth laws, regulations and rules on non-Federal land located within the boundary of the Historical Park.\n##### (c) No net loss of commonwealth owned buildings and structures\nIn the event of loss or authorized demolition of buildings or structures within the Fort Monroe National Historic Landmark District, replacement of the square footage from such loss or demolition shall be permitted provided that such construction complies with the Secretary\u2019s Standards for the Treatment of Historic Properties, and section 306108 of title 54, United States Code (formerly section 106 of the National Historic Preservation Act), as applicable.\n##### (d) Authorization of ex-Officio appointments\nThe Superintendent of the Historical Park is authorized to serve as an ex-officio member of such boards or committees affecting Fort Monroe that the Secretary considers beneficial to the preservation of Historical Park resources and which further the interpretive or educational purposes of the Historical Park.\n##### (e) Cooperative agreements\nThe Secretary may enter into cooperative agreements with the Commonwealth or other public or private entities to identify, interpret, and provide financial and technical assistance for the preservation of non-Federal resources within the boundary of the Historical Park and outside of the boundary in close proximity to the Historical Park provided that\u2014\n**(1)**\nany cooperative agreement entered into to provide assistance to non-Federal land shall provide for reasonable public access to the non-Federal land;\n**(2)**\nno changes or alterations shall be made to the exterior of the properties except by mutual agreement of the other parties to the agreements; and\n**(3)**\nthe Federal share of the total cost of any activity carried out under the agreement shall be not more than 50 percent, with in-kind contributions or goods or services fairly valued authorized, as appropriate, for the non-Federal share.\n##### (f) Adaptive reuse\nNothing in this Act shall be construed to inhibit the Commonwealth from providing for the adaptive reuse of the interior of any non-federally owned historic resource in accordance with the Secretary\u2019s Standards for the Treatment of Historic Properties.",
      "versionDate": "2025-02-25",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Conflicts and wars",
            "updateDate": "2026-02-06T19:33:50Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2026-02-06T19:33:12Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2026-02-06T19:33:55Z"
          },
          {
            "name": "Military history",
            "updateDate": "2026-02-06T19:33:32Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2026-02-06T19:34:00Z"
          },
          {
            "name": "Parks, recreation areas, trails",
            "updateDate": "2026-02-06T19:33:07Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-02-06T19:34:05Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-02-06T19:33:26Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2026-02-06T19:33:45Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2026-02-06T19:33:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-09T21:29:39Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1581ih.xml"
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
      "title": "Fort Monroe National Historical Park Establishment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fort Monroe National Historical Park Establishment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Fort Monroe National Historical Park in the Commonwealth of Virginia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:48Z"
    }
  ]
}
```
