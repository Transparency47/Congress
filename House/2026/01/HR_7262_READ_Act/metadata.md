# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7262
- Title: READ Act
- Congress: 119
- Bill type: HR
- Bill number: 7262
- Origin chamber: House
- Introduced date: 2026-01-27
- Update date: 2026-02-13T17:11:52Z
- Update date including text: 2026-02-13T17:11:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-01-27: Introduced in House

## Actions

- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Introduced in House
- 2026-01-27 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7262",
    "number": "7262",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001231",
        "district": "22",
        "firstName": "John",
        "fullName": "Rep. Mannion, John W. [D-NY-22]",
        "lastName": "Mannion",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "READ Act",
    "type": "HR",
    "updateDate": "2026-02-13T17:11:52Z",
    "updateDateIncludingText": "2026-02-13T17:11:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-27",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T17:30:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "LA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7262ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7262\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 27, 2026 Mr. Mannion (for himself, Mr. Carter of Louisiana , and Ms. Chu ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo authorize the Secretary of Education to make payments to State educational agencies to provide immediate services or assistance to local educational agencies and non-public schools that serve an area in which a major disaster or emergency has been declared, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restarting Education After Disasters Act or the READ Act .\n#### 2. Immediate aid to restart school operations\n##### (a) Payments authorized\n**(1) In general**\nFrom amounts appropriated to carry out this section, the Secretary is authorized to make payments, on such basis as the Secretary determines appropriate, to State educational agencies to enable such agencies to provide services or assistance to local educational agencies or non-public schools serving an area in which a covered disaster or emergency has been declared.\n**(2) Enrollment**\nIn determining the amount to be provided in payments authorized under paragraph (1), the Secretary shall\u2014\n**(A)**\ntake into consideration the number of students who were enrolled, during the school year immediately preceding the school year in which a covered disaster or emergency occurred, in elementary schools and secondary schools that were closed as a result of such covered disaster or emergency; and\n**(B)**\ngive priority to State educational agencies serving elementary schools and secondary schools that were not used for educational instruction for 30 or more days.\n##### (b) Eligibility, consideration, and equity\n**(1) Eligibility and consideration**\nFrom the payment provided by the Secretary under subsection (a), the State educational agency shall provide services and assistance to local educational agencies and non-public schools, consistent with the provisions of this section. In determining the amount to be provided for services or assistance under this section, the State educational agency shall consider the following:\n**(A)**\nThe number of school-aged children served by the local educational agency or non-public school in the academic year preceding the academic year for which the services or assistance are provided.\n**(B)**\nThe severity of the impact of the covered disaster or emergency on the local educational agency or nonpublic school and the extent of the needs in each local educational agency or non-public school that is in an area in which a covered disaster or emergency has been declared.\n**(2) Equity**\nEducational services and assistance provided for eligible non-public school students under paragraph (1) shall be equitable in comparison to the educational services and other benefits provided for public school students under this section, and shall be provided in a timely manner.\n##### (c) Applications\nEach local educational agency or non-public school desiring services or assistance under this section shall submit an application to the State educational agency at such time, in such manner, and accompanied by such information as the State educational agency may reasonably require to ensure expedited and timely provision of services or assistance to the local educational agency or non-public school.\n##### (d) Uses of funds\n**(1) In general**\nA local educational agency or non-public school receiving services or assistance from the State educational agency under this section shall use such services or assistance for\u2014\n**(A)**\nrecovery of student and personnel data, and other electronic information;\n**(B)**\nreplacement of school district information systems, including hardware and software;\n**(C)**\nfinancial operations;\n**(D)**\nreasonable transportation costs;\n**(E)**\nrental of mobile educational units and leasing of neutral sites or spaces;\n**(F)**\ninitial replacement of instructional materials and equipment, including textbooks;\n**(G)**\nredeveloping instructional plans, including curriculum development;\n**(H)**\ninitiating and maintaining education and support services;\n**(I)**\nfacility and equipment repairs and minor renovation of schools; and\n**(J)**\nsuch other activities related to the purpose of this section that are approved by the Secretary.\n**(2) Use with other available funds**\nA local educational agency or non-public school receiving services or assistance under this section may use such services or assistance in coordination with other Federal, State, or local funds available for the activities described in paragraph (1).\n**(3) Special rules**\n**(A) Prohibition**\nServices or assistance provided under this section shall not be used for construction or major renovation of schools.\n**(B) Secular, neutral, and nonideological services or assistance**\nServices or assistance provided under this section, including equipment and materials, shall be secular, neutral, and nonideological.\n##### (e) Supplement not supplant\n**(1) In general**\nExcept as provided in paragraph (2), services or assistance made available under this section shall be used to supplement, not supplant, any funds made available through the Federal Emergency Management Agency or through a State.\n**(2) Exception**\nParagraph (1) shall not prohibit the provision of Federal assistance under this section to an eligible State educational agency, local educational agency, or nonpublic school that is or may be entitled to receive, from another source, benefits for the same purposes as under this section if\u2014\n**(A)**\nsuch State educational agency, local educational agency, or school has not received such other benefits by the time of application for Federal assistance under this section; and\n**(B)**\nsuch State educational agency, local educational agency, or school agrees to repay all duplicative Federal assistance received to carry out the purposes of this section.\n##### (f) Assistance to non-Public schools\n**(1) Funds availability**\n**(A) In general**\nFrom the payment provided by the Secretary under subsection (b) to a State educational agency, the State educational agency shall reserve an amount of funds, to be made available to non-public schools in the State, that is not less than an amount that bears the same relation to the payment as the number of students in non-public elementary schools and secondary schools in the State bears to the total number of students in non-public and public elementary schools and secondary schools in the State.\n**(B) Number of schools**\nThe number of students in schools described in subparagraph (A) shall be determined by the National Center for Education Statistics Common Core of Data for the most recent school year for which data is available.\n**(C) Use of funds**\nExcept as provided in paragraph (2), the funds reserved under subparagraph (A) shall be used for the provision of services or assistance at non-public schools.\n**(2) Special rule**\nIf funds reserved under paragraph (1) remain unobligated 120 days after the date of enactment of this section, such funds may be used to provide services or assistance under this section to local educational agencies.\n**(3) Public control of funds**\nThe control of funds for the services and assistance provided to a non-public school under paragraph (1), and title to materials, equipment, and property purchased with such funds, shall be in a public agency, and a public agency shall administer such funds, materials, equipment, and property and shall provide such services (or may contract for the provision of such services with a public or private entity).\n##### (g) Definitions\nIn this section:\n**(1) Covered disaster or emergency**\nThe term covered disaster or emergency means a major disaster or emergency that has been declared\u2014\n**(A)**\nin accordance with section 401 or 501 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 ; 5190); or\n**(B)**\nby the State served by such State educational agency, in accordance with State law.\n**(2) ESEA terms**\nThe terms elementary school , local educational agency , secondary school , Secretary , and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(3) Non-public school**\nThe term non-public school means a non-public elementary school or secondary school that\u2014\n**(A)**\nis accredited or licensed or otherwise operates in accordance with State law; and\n**(B)**\nwas in existence on the date that is 1 week prior to the date that the major disaster or emergency was declared for the area.\n##### (h) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section $200,000,000 for each of fiscal years 2026 through 2030, to remain available until expended.",
      "versionDate": "2026-01-27",
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
        "name": "Education",
        "updateDate": "2026-02-13T17:11:51Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7262ih.xml"
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
      "title": "READ Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "READ Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restarting Education After Disasters Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Education to make payments to State educational agencies to provide immediate services or assistance to local educational agencies and non-public schools that serve an area in which a major disaster or emergency has been declared, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:35Z"
    }
  ]
}
```
