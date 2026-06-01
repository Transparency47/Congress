# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4881?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4881
- Title: SWIFT VOTE Act
- Congress: 119
- Bill type: HR
- Bill number: 4881
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2026-03-04T09:06:12Z
- Update date including text: 2026-03-04T09:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4881",
    "number": "4881",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001130",
        "district": "30",
        "firstName": "Jasmine",
        "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
        "lastName": "Crockett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "SWIFT VOTE Act",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:12Z",
    "updateDateIncludingText": "2026-03-04T09:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:00:30Z",
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
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "PA"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "LA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
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
      "sponsorshipDate": "2025-08-05",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "DC"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "MS"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "PA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "MI"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4881ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4881\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Ms. Crockett (for herself, Ms. Williams of Georgia , Mr. Deluzio , Mr. Evans of Pennsylvania , Mr. Fields , Mr. Goldman of New York , Mr. Johnson of Georgia , Ms. Norton , and Mr. Thompson of Mississippi ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo direct the Election Assistance Commission to make grants to States for procuring and maintaining electronic pollbooks with the capability of collecting and disseminating wait time information, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Supplying Wait-time Information to Facilitate Timely Voting with Operational and Technology Enhancements Act or the SWIFT VOTE Act .\n#### 2. Grants for procuring and maintaining electronic pollbooks\n##### (a) Grants\n**(1) Authority to make grants**\nNot later than 1 year after the date of the enactment of this Act, the Election Assistance Commission shall make a grant to each eligible jurisdiction in a State for the purpose of\u2014\n**(A)**\nprocuring or maintaining electronic pollbooks (hereafter referred to as e-pollbooks ); or\n**(B)**\ndeveloping the capability of collecting and disseminating wait time information for use in elections for Federal office, whether through the use of e-pollbooks with such capability or through other means.\n**(2) Prioritization of grants to procure e-pollbooks**\nIn making grants to eligible jurisdictions under this section, the Commission shall give priority to eligible jurisdictions showing demonstrated need for new or additional e-pollbooks which the jurisdiction will use to reduce wait times at polling places on the dates of elections for Federal office, and give priority to eligible jurisdictions that propose the development of capability to report wait time information in accordance with subsection (c)(2)(A).\n##### (b) Eligibility\nAn eligible jurisdiction is eligible to receive a grant under this section if the eligible jurisdiction submits to the Commission, at such time and in such form as the Commission may require, an application containing the information and assurances described in subsection (c).\n##### (c) Information described\nThe information and assurances described in this subsection are, with respect to an eligible jurisdiction, the following:\n**(1)**\nFor an eligible jurisdiction seeking funding for e-pollbooks, a description of the need of the eligible jurisdiction for procuring or maintaining e-pollbooks.\n**(2)**\nFor an eligible jurisdiction seeking funding for the collection and dissemination of wait time information\u2014\n**(A)**\na certification that the chief election official of the eligible jurisdiction shall publish on the official public website of the chief election official the most recent wait time information for each polling place which is open for voters to vote in an election for Federal office\u2014\n**(i)**\nin the case of a polling place which is open for 4 hours or fewer on such a day, on an hourly basis on such a day; or\n**(ii)**\nin the case of a polling place which is open for more than 4 hours on such a day, on at least 4 regular intervals on such a day.\n**(B)**\nFollowing each election cycle, publish on the official public website of the chief election official of the eligible jurisdiction a report detailing wait time information through that election cycle, including on the date of the election as well as any dates on which individuals were permitted to vote in person prior to the date of the election, including wait times throughout each such day of voting, to the extent such information is available.\n**(3)**\nAn assurance that\u2014\n**(A)**\nthe funds provided under this section will be used to supplement and not supplant other funds used to carry out the activities for which the funds are provided; and\n**(B)**\nthe chief election official of the eligible jurisdiction shall provide regular reports to the Commission containing information on the procurement and maintenance of e-pollbooks with the funds provided under this section.\n**(4)**\nAn assurance that the eligible jurisdiction shall develop procedures for certifying that the procurement and maintenance of e-pollbooks with the funds provided under this section is in compliance with the Commission\u2019s Voluntary Electronic Poll Book Certification Program, or any similar or successor program established by the Commission for e-pollbook certification. Nothing in this paragraph may be construed to prohibit a eligible jurisdiction in a State from receiving a grant under this section on the grounds that the State has in effect standards and procedures for the use of e-pollbooks which are in addition to the standards and procedures required by the Commission.\n**(5)**\nAn assurance that the eligible jurisdiction will work with experts in voting system technology and infrastructure to develop and carry out training programs in the use of e-pollbooks by election officials, and that such programs will train election officials in methods that will enable the officials to meet the needs of individual voters, including voters with limited English language proficiency and voters with disabilities, without regard to age, gender, or sexual orientation.\n**(6)**\nSuch other information and assurances as the Commission may require.\n##### (d) Definitions\nIn this section, the following definitions apply:\n**(1)**\nThe term Commission means the Election Assistance Commission.\n**(2)**\nThe term election cycle means the period beginning on the day after the date of the most recent regularly scheduled general election for Federal office and ending on the date of the next such election.\n**(3)**\nThe term eligible jurisdiction means a State or a political subdivision of a State which is responsible for carrying out an election for Federal office in the State.\n**(4)**\nThe term e-pollbook means a device or technology that may be used at a polling place in an election for Federal office in place of a traditional paper poll book and that partially automates the process of checking in voters, assigning voters the correct ballot style, and tracking voters who have been issued a ballot. An e-pollbook may be used at the polling place together with a separate copy of the list of registered voters or may be networked into a central voter registration system which enables the election official at the polling place to check and update voter records in real time.\n**(5)**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, Guam, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands.\n**(6)**\nThe term wait time information means, with respect to a polling place in an election for Federal office, the length of time between when an individual arrives at the polling place and completes the polling place\u2019s check-in process, as well as the length of time between the completion of that individual\u2019s check-in process and when that individual receives a ballot or, if a physical ballot is not provided, until the individual is directed to an electronic voting machine.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $120,000,000, to remain available until expended.",
      "versionDate": "2025-08-05",
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
        "updateDate": "2025-09-15T18:14:10Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4881ih.xml"
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
      "title": "SWIFT VOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SWIFT VOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supplying Wait-time Information to Facilitate Timely Voting with Operational and Technology Enhancements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Election Assistance Commission to make grants to States for procuring and maintaining electronic pollbooks with the capability of collecting and disseminating wait time information, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:36Z"
    }
  ]
}
```
