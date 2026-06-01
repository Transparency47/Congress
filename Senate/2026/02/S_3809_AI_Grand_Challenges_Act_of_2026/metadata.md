# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3809?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3809
- Title: AI Grand Challenges Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3809
- Origin chamber: Senate
- Introduced date: 2026-02-09
- Update date: 2026-05-21T20:41:58Z
- Update date including text: 2026-05-21T20:41:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in Senate
- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-02-09: Introduced in Senate

## Actions

- 2026-02-09 - IntroReferral: Introduced in Senate
- 2026-02-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3809",
    "number": "3809",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "AI Grand Challenges Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T20:41:58Z",
    "updateDateIncludingText": "2026-05-21T20:41:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-09",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-02-09T22:54:59Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "SD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3809is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3809\nIN THE SENATE OF THE UNITED STATES\nFebruary 9, 2026 Mr. Booker (for himself, Mr. Rounds , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo authorize the Director of the National Science Foundation to identify grand challenges and award competitive prizes for artificial intelligence research and development.\n#### 1. Short title\nThis Act may be cited as the AI Grand Challenges Act of 2026 .\n#### 2. Prize competitions for artificial intelligence research and development\n##### (a) Definition\nExcept as otherwise expressly provided, in this section the term Director means the Director of the National Science Foundation.\n##### (b) Establishment of program\n**(1) In general**\nNot later than 12 months after the date of enactment of this Act, the Director, in coordination with the National Artificial Intelligence Advisory Committee, shall establish a program to award prizes, utilizing the authorities and processes established under section 24 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719 ), to eligible participants as determined by the Director pursuant to subsection (e) to stimulate artificial intelligence research, development, and commercialization that solves or advances specific, well-defined, and measurable grand challenges in 1 or more of the following categories:\n**(A)**\nNational security.\n**(B)**\nCybersecurity.\n**(C)**\nHealth.\n**(D)**\nEnergy.\n**(E)**\nEnvironment.\n**(F)**\nTransportation.\n**(G)**\nAgriculture and rural development.\n**(H)**\nEducation and workforce training.\n**(I)**\nManufacturing.\n**(J)**\nSpace and aerospace.\n**(K)**\nQuantum computing, including molecular modeling and simulation.\n**(L)**\nMaterials science.\n**(M)**\nSupply chain resilience.\n**(N)**\nDisaster preparedness.\n**(O)**\nNatural resources management.\n**(P)**\nCross-cutting challenges in artificial intelligence, including robustness, interpretability, explainability, transparency, safety, privacy, content provenance, and bias mitigation.\n**(2) Designation**\nThe grand challenges and prize competition program established under paragraph (1) shall be known as the AI Grand Challenges Program .\n**(3) Rotators**\nParticipants in the Rotator Program of the National Science Foundation may support the development and implementation of the AI Grand Challenges Program.\n##### (c) Grand challenges selection and grand challenges information\n**(1) In general**\n**(A) Consultation on identification and selection**\nThe Director shall consult with the Director of the Office of Science and Technology Policy, and may consult with the Director of the National Institute of Standards and Technology, the Director of the Defense Advanced Research Projects Agency, the heads of relevant Federal agencies, and the National Artificial Intelligence Advisory Committee, to identify and select artificial intelligence research and development grand challenges in which eligible participants will compete to solve or advance for prize awards under subsection (b).\n**(B) Public input on identification**\nThe Director shall also seek public input on the identification of artificial intelligence research and development grand challenges.\n**(2) Problem statements; success metrics**\nFor each grand challenge selected under paragraph (1) and the grand challenge under paragraph (3), the Director shall\u2014\n**(A)**\nestablish a specific and well-defined grand challenge problem statement and ensure that such problem statement is published on the National Science Foundation website linking out to relevant prize competition listings on the website Challenge.gov that is managed by the General Services Administration; and\n**(B)**\nestablish and publish on the website Challenge.gov clear targets, the challenge process (which may include a multi-stage process), success metrics, and validation protocols for the prize competitions designed to address each grand challenge, in order to provide specific benchmarks that will be used to evaluate submissions to the prize competition.\n**(3) Grand challenge for artificial intelligence-enabled cancer breakthroughs**\n**(A) Required prize competition**\nNot later than 1 year after the date of enactment of this Act, the Director, in consultation with the Director of the Office of Science and Technology Policy and the Director of the National Institutes of Health, shall establish not less than 1 grand challenge in which eligible participants will compete in a prize competition to solve or advance solutions for prize awards under subsection (b) that seek to advance medical breakthroughs to address 1 or more of the most lethal forms of cancer and related comorbidities. The grand challenge shall relate to detection, diagnostics, treatments, therapeutics, or other innovations in artificial intelligence to increase the total quality-adjusted life years of those affected or likely to be affected by cancer.\n**(B) Prize amount**\nIn carrying out the prize competition under subparagraph (A), the Director shall award not less than $10,000,000 in cash prize awards to each winner.\n**(4) Ambitious and achievable goals**\nGrand challenges selected under paragraph (1) and the grand challenge under paragraph (3) shall be ambitious but achievable goals that utilize science, technology, and innovation to solve or advance solutions to problems to benefit the United States.\n##### (d) Additional consultation\nThe Director may consult with, and incorporate effective practices from, other entities that have developed successful large-scale technology demonstration prize competitions, including the Defense Advanced Research Projects Agency, the National Aeronautics and Space Administration, other Federal agencies, private sector enterprises, and nonprofit organizations, in the development and implementation of the AI Grand Challenges Program and related prize competitions, including on the requirements under subsection (e).\n##### (e) Requirements\n**(1) In general**\nThe Director shall develop requirements for\u2014\n**(A)**\nthe prize competition process, including eligibility criteria for participants, consistent with the requirements under paragraph (2); and\n**(B)**\ntesting, judging, and verification procedures for submissions to receive a prize award under the AI Grand Challenges Program.\n**(2) Eligibility requirement and judging**\n**(A) Eligibility**\nIn accordance with the requirement described in section 24(g)(3) of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719(g)(3) ), a recipient of a prize award under the AI Grand Challenges Program\u2014\n**(i)**\nthat is a private entity shall be incorporated in and maintain a primary place of business in the United States; and\n**(ii)**\nwho is an individual, whether participating singly or in a group, shall be a citizen or permanent resident of the United States.\n**(B) Judges**\nIn accordance with section 24(k) of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719(k) ), a judge of a prize competition under the AI Grand Challenges Program may be an individual from the private sector.\n##### (f) Prize amount\n**(1) In general**\nIn carrying out the AI Grand Challenges Program, the Director\u2014\n**(A)**\nshall award not less than $1,000,000 in cash prize awards to each winner of the prize competitions, except as provided in subsection (c)(3); and\n**(B)**\nmay also utilize non-cash awards.\n**(2) Larger awards**\nThe Director may award prizes under the AI Grand Challenges Program that are more than $50,000,000, pursuant to the requirements under section 24(m)(4)(A) of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719(m)(4)(A) ).\n##### (g) Funding\n**(1) In general**\nIn accordance with section 24(m)(1) of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3719(m)(1) ), the Director may request and accept funds from other Federal agencies, State, United States territory, local, or Tribal government agencies, for-profit entities, and nonprofit entities to support the AI Grand Challenges Program.\n**(2) Prohibition on consideration for support**\nThe Director may not consider any support provided by an agency or entity under paragraph (1) in determining the winners of prize awards under subsection (b).\n##### (h) Reports\n**(1) Notification of winning submission**\nNot later than 60 days after the date on which a prize is awarded under the AI Grand Challenges Program, the Director shall submit to the Committee on Commerce, Science, and Transportation of the Senate, the Committee on Science, Space, and Technology of the House of Representatives, and other relevant committees of Congress a report that describes the winning submission to the prize competition and its benefits to the United States.\n**(2) Biennial report**\n**(A) In general**\nNot later than 2 years after the date of enactment of this Act, and biennially thereafter, the Director shall submit to the Committee on Commerce, Science, and Transportation of the Senate, the Committee on Science, Space, and Technology of the House of Representatives, and other relevant committees of Congress a report that includes\u2014\n**(i)**\na description of the activities carried out under this Act;\n**(ii)**\na description of the active competitions and the results of completed competitions under the AI Grand Challenges Program; and\n**(iii)**\nefforts to provide information to the public about the AI Grand Challenges Program to encourage participation.\n**(B) Public accessibility**\nThe Director shall make the biennial report required under subparagraph (A) publicly accessible, including by posting the biennial report on the website of the National Science Foundation in an easily accessible location.\n##### (i) Accessibility\nIn carrying out the AI Grand Challenges Program, the Director shall post the active prize competitions and available prize awards under subsection (b) to Challenge.gov after the grand challenges are selected and the prize competitions are designed pursuant to subsections (c) and (e) to ensure the prize competitions are widely accessible to eligible participants.\n#### 3. Coordination on Federal publication of grand challenge data sets\nThe Director of the Office of Science and Technology Policy shall coordinate Federal agencies that fund science to identify and publish data sets for grand challenges that\u2014\n**(1)**\naddress foundational scientific problems that if addressed would significantly advance scientific understanding; and\n**(2)**\ncan be addressed through innovation from the use of artificial intelligence.",
      "versionDate": "2026-02-09",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-02-09",
        "text": "Referred to the House Committee on Science, Space, and Technology."
      },
      "number": "7434",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AI Grand Challenges Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-27",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Energy and Commerce, Agriculture, Oversight and Government Reform, Education and Workforce, the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Leadership in AI Act",
      "type": "HR"
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
        "updateDate": "2026-02-27T19:38:15Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3809is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "AI Grand Challenges Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T06:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI Grand Challenges Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize the Director of the National Science Foundation to identify grand challenges and award competitive prizes for artificial intelligence research and development.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T06:18:28Z"
    }
  ]
}
```
