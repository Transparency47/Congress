# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7943?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7943
- Title: Communications Equity and Diversity Council Act
- Congress: 119
- Bill type: HR
- Bill number: 7943
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-02T19:24:29Z
- Update date including text: 2026-04-02T19:24:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7943",
    "number": "7943",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "M001226",
        "district": "8",
        "firstName": "Robert",
        "fullName": "Rep. Menendez, Robert [D-NJ-8]",
        "lastName": "Menendez",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Communications Equity and Diversity Council Act",
    "type": "HR",
    "updateDate": "2026-04-02T19:24:29Z",
    "updateDateIncludingText": "2026-04-02T19:24:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
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
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:00:15Z",
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
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "CA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7943ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7943\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mr. Menendez (for himself, Ms. Matsui , Ms. Barrag\u00e1n , and Mr. Carter of Louisiana ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo establish within the Federal Communications Commission the Communications Equity and Diversity Council, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Communications Equity and Diversity Council Act .\n#### 2. Communications Equity and Diversity Council\n##### (a) Establishment\nThere is established within the Commission an advisory committee to be known as the Communications Equity and Diversity Council.\n##### (b) Duties\nThe duties of the Council shall be the following:\n**(1)**\nTo make recommendations to the Commission, including with respect to\u2014\n**(A)**\nadvancing equity with respect to the provision of and access to communication services, without discrimination on the basis of race, color, religion, national origin, sex, or disability;\n**(B)**\nassisting historically underserved individuals to benefit from communication services and opportunities made possible by such services;\n**(C)**\naccelerating the deployment to all communities of affordable and reliable communication services by reducing or removing regulatory barriers to infrastructure and investment;\n**(D)**\naccelerating the entry of small businesses, including those owned by historically underserved individuals, into industries relating to communication services; and\n**(E)**\npromoting, with respect to communication services, a diversity of voices, localism, economic competition, technological advancement, and the public interest, convenience, and necessity.\n**(2)**\nTo provide a forum for stakeholders with respect to communication services, including with respect to the issues of\u2014\n**(A)**\ndeployment;\n**(B)**\naffordability;\n**(C)**\ndigital discrimination;\n**(D)**\naccess to capital;\n**(E)**\nsmall business mentoring;\n**(F)**\nemployment upskilling;\n**(G)**\nownership diversity; and\n**(H)**\nprocurement opportunities.\n**(3)**\nTo develop data and examine industry trends and practices for purposes of carrying out each duty described in this subsection.\n**(4)**\nTo carry out other tasks as determined appropriate by the Commission.\n##### (c) Membership\n**(1) Number and appointment**\nThe Council shall be composed of not fewer than 30 and not more than 35 members, each of whom shall be appointed by the Chair of the Commission.\n**(2) Term**\nEach member of the Council shall serve for a 2-year term.\n**(3) Representation**\nThe members of the Council shall\u2014\n**(A)**\nbe appointed in a manner that ensures the Council has the expertise and balance of viewpoints necessary to carry out the duties of the Council; and\n**(B)**\ninclude representatives of\u2014\n**(i)**\nhistorically underserved individuals;\n**(ii)**\nconsumers;\n**(iii)**\ncivil rights organizations; and\n**(iv)**\nindustry stakeholders with respect to communication services.\n**(4) Designated Federal Officer**\n**(A) Appointment**\nThe Chair of the Commission shall appoint an employee of the Commission as the Designated Federal Officer for purposes of the Council.\n**(B) Duties**\nThe Designated Federal Officer appointed under subparagraph (A) shall\u2014\n**(i)**\ncall or approve each meeting of the Council;\n**(ii)**\nprepare and approve each meeting agenda;\n**(iii)**\nattend each meeting of the Council;\n**(iv)**\nadjourn each meeting of the Council once the Designated Federal Officer determines adjournment is in the public interest; and\n**(v)**\nchair each meeting of the Council when directed to do so by the Chair of the Commission.\n**(5) Vacancies**\nThe Chair of the Commission shall fill any vacancy of the Council within 60 days from the date an appointment of the Council becomes vacant.\n##### (d) Meetings\n**(1) In general**\nThe Council shall meet not fewer than 3 times each year.\n**(2) Open meeting requirements**\nEach meeting of the Council shall\u2014\n**(A)**\nbe open to the public; and\n**(B)**\nresult in a deliverable, accessible to the public, including\u2014\n**(i)**\nany recommendation made to the Council;\n**(ii)**\na summary of the meeting;\n**(iii)**\nmeeting minutes; and\n**(iv)**\na presentation of any topic discussed.\n**(3) Notice**\nTimely notice of each meeting of the Council shall be published in the Federal Register.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $450,000 for fiscal year 2027.\n##### (f) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Council**\nThe term Council means the Communications Equity and Diversity Council established under subsection (a).\n**(3) Communication service**\nThe term communication service means communication services subject to the jurisdiction of the Federal Communications Commission.\n**(4) Historically underserved individual**\nThe term historically underserved individual means each of the following:\n**(A)**\nAn individual of color.\n**(B)**\nA woman.\n**(C)**\nAn individual who resides in a rural area.\n**(D)**\nA veteran.\n**(E)**\nAn individual with a disability.\n**(F)**\nAn individual adversely affected by persistent poverty or inequality.\n**(5) Rural**\nThe term rural has the meaning given such term in section 54.600 of title 47, Code of Federal Regulations (or any successor regulation).",
      "versionDate": "2026-03-16",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-04-02T19:24:28Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7943ih.xml"
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
      "title": "Communications Equity and Diversity Council Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Communications Equity and Diversity Council Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-01T07:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish within the Federal Communications Commission the Communications Equity and Diversity Council, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-01T07:18:22Z"
    }
  ]
}
```
