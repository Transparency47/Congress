# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2971?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2971
- Title: YOUNG Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2971
- Origin chamber: House
- Introduced date: 2025-04-21
- Update date: 2025-06-24T08:05:17Z
- Update date including text: 2025-06-24T08:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-21: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-04-21: Introduced in House

## Actions

- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-21",
    "latestAction": {
      "actionDate": "2025-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2971",
    "number": "2971",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "YOUNG Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-24T08:05:17Z",
    "updateDateIncludingText": "2025-06-24T08:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
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
      "actionDate": "2025-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-21",
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
          "date": "2025-04-21T16:00:05Z",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2971ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2971\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2025 Ms. Ansari (for herself, Mr. Huffman , and Ms. Matsui ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of Commerce to establish a youth biodiversity monitoring grant program.\n#### 1. Short title\nThis Act may be cited as the Youth Outdoors Using Nature\u2019s Genetics Act of 2025 or the YOUNG Act of 2025 .\n#### 2. Youth biodiversity monitoring grant program\n##### (a) In general\nThe Secretary, in coordination with the heads of relevant Federal agencies, including the Director of the United States Geological Survey and the Director of the United States Fish and Wildlife Service, shall establish a grant program to award amounts and provide technical assistance to covered entities to carry out youth biodiversity monitoring projects that use and educate students about advanced technologies.\n##### (b) Applications\nTo be eligible for a grant under this section, a covered entity shall submit to the Secretary an application in such form, at such time, and containing such information as the Secretary determines appropriate.\n##### (c) Use of amounts\nA covered entity that is awarded a grant under this section may use such grant to carry out the following activities as part of a youth biodiversity monitoring project:\n**(1)**\nThe purchase of supplies.\n**(2)**\nTransportation of participants to and from a youth biodiveristy monitoring project.\n**(3)**\nOutreach with respect to a youth biodiversity monitoring project to promote participation in such project.\n**(4)**\nThe purchase of scientific collection licenses and permits.\n**(5)**\nOther expenses related to carrying out a youth biodiversity monitoring project the Secretary determines appropriate.\n##### (d) Priority\nIn awarding grants under this section, the Secretary shall give priority to applications from covered entities that include a proposal for a youth biodiversity monitoring project focused on an underserved community.\n##### (e) Report\nNot later than 2 years after the date of the enactment of this section, the Secretary shall submit to Congress a report regarding the grant program, including the following information:\n**(1)**\nEach eligible entity awarded a grant under this section.\n**(2)**\nThe amount awarded to each such eligible entity.\n**(3)**\nHow each such eligible entity used such grant.\n**(4)**\nThe number of participants in youth biodiversity monitoring projects carried out using grants awarded under this section.\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated to the Secretary to carry out this section $1,000,000 for each of fiscal years 2026 through 2032.\n##### (g) Definitions\nIn this section:\n**(1) Advanced technologies**\nThe term advanced technologies means\u2014\n**(A)**\nenvironmental DNA collection and analysis procedures;\n**(B)**\nremote sensing;\n**(C)**\ndrones;\n**(D)**\ncamera traps;\n**(E)**\nacoustic monitoring;\n**(F)**\nadvanced sensors and sensor networks;\n**(G)**\nAI, machine learning, or advanced modeling; or\n**(H)**\nany other technology or method the Secretary determines appropriate.\n**(2) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na nonprofit organization;\n**(B)**\nan elementary school or secondary school (as those terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ));\n**(C)**\nan institution of higher education (as that term is defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 )); or\n**(D)**\na State, local, or Tribal government.\n**(3) Grant program**\nThe term grant program means the grant program established pursuant to subsection (a).\n**(4) Nonprofit organization**\nThe term nonprofit organization means an organization that is\u2014\n**(A)**\ndescribed in section 501(c)(3) of the Internal Revenue Code of 1986; and\n**(B)**\nexempt from taxation under section 501(a) of that Code.\n**(5) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Under Secretary of Commerce for Oceans and Atmosphere.\n**(6) State**\nThe term State means\u2014\n**(A)**\neach of the several States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico;\n**(D)**\nAmerican Samoa;\n**(E)**\nGuam;\n**(F)**\nthe Commonwealth of the Northern Mariana Islands;\n**(G)**\nthe Virgin Islands of the United States; and\n**(H)**\nany other territory or possession of the United States.\n**(7) Tribal government**\nThe term Tribal government means the recognized governing body of any Indian or Alaska Native Tribe, band, nation, pueblo, village, community, component band, or component reservation individually identified (including parenthetically) in the list published pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ).\n**(8) Underserved community**\nThe term underserved community means a population of individuals sharing a particular characteristic, or a geographic community, that has been systematically denied a full opportunity to participate in aspects of economic, social, or civic life, such as\u2014\n**(A)**\nracial and ethnic minorities;\n**(B)**\nindividuals with access and functional needs; or\n**(C)**\nindividuals otherwise adversely affected by persistent poverty or inequality.\n**(9) Youth biodiversity monitoring project**\nThe term youth biodiversity monitoring project means a project that provides youth with\u2014\n**(A)**\nhands-on experience collecting, analyzing, or interpreting biological data about wildlife populations and the ecosystems associated with such populations; and\n**(B)**\neducation regarding\u2014\n**(i)**\nwildlife science;\n**(ii)**\nmarine science;\n**(iii)**\nconservation; or\n**(iv)**\nbiodiversity.",
      "versionDate": "2025-04-21",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-20T14:50:32Z"
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
      "date": "2025-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2971ih.xml"
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
      "title": "YOUNG Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "YOUNG Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Youth Outdoors Using Nature\u2019s Genetics Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Commerce to establish a youth biodiversity monitoring grant program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T03:03:23Z"
    }
  ]
}
```
