# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7907?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7907
- Title: AI-Ready Bio-Data Standards Act
- Congress: 119
- Bill type: HR
- Bill number: 7907
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:09:00Z
- Update date including text: 2026-04-02T18:09:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-03-12: Introduced in House

## Actions

- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7907",
    "number": "7907",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "AI-Ready Bio-Data Standards Act",
    "type": "HR",
    "updateDate": "2026-04-02T18:09:00Z",
    "updateDateIncludingText": "2026-04-02T18:09:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:31:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7907ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7907\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Mr. Khanna (for himself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo direct the Director of the National Institute of Standards and Technology to facilitate the establishment of definitions, standards, resources, and frameworks to ensure certain biological datasets are ready for use in artificial intelligence models, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI-Ready Bio-Data Standards Act .\n#### 2. Definitions, standards, resources, and frameworks by the National Institute of Standards and Technology for certain biological datasets\n##### (a) Establishment\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Director of the National Institute of Standards and Technology (in this section referred to as the Director ), pursuant to recommendations from the advisory group under subsection (f) and taking into account any feedback received under subsection (e), shall facilitate the establishment of definitions, standards, resources, and frameworks to ensure each biological dataset generated as a result of qualified federally funded research is artificial intelligence-ready.\n**(2) Requirements for definitions, standards, resources, and frameworks**\n**(A) Definitions**\n**(i) In general**\nIn carrying out paragraph (1), the Director shall facilitate the establishment of definitions for the following terms:\n**(I)**\nArtificial intelligence-ready.\n**(II)**\nBiomanufacturing.\n**(III)**\nBiotechnology.\n**(IV)**\nQualified federally funded research.\n**(ii) Requirements for definition of artificial intelligence-ready**\n**(I) In general**\nIn facilitating the establishment of the definition of the term artificial intelligence-ready under clause (i)(I), the Director shall take such actions as may be necessary to ensure such definition, when applied to a biological dataset, requires such dataset be generated and formatted in a manner that\u2014\n**(aa)**\nenables the effective use of the dataset for training artificial intelligence models; and\n**(bb)**\nsupports advancements in research relating to artificial intelligence and biotechnology.\n**(II) Discretion**\nWith respect to a biological dataset that otherwise satisfies the definition of artificial intelligence-ready under clause (i)(I), the Director may, in consultation with the Chief Data Officer of the Federal department or agency that is responsible for such biological dataset, determine that such dataset is not artificial intelligence-ready.\n**(iii) Requirements for definition of qualified federally funded research**\nIn facilitating the establishment of the definition of the term qualified federally funded research under clause (i)(IV), the Director shall take such actions as may be necessary to include in such definition certain conditions that, if satisfied, will result in certain federally funded research being qualified federally funded research. Such conditions shall include the following:\n**(I)**\nThe amount of Federal funding awarded to a recipient.\n**(II)**\nThe capability of the recipient to generate a biological dataset that is artificial intelligence-ready.\n**(III)**\nThe expertise of the recipient in generating a biological dataset that is artificial intelligence-ready.\n**(IV)**\nThe size of the biological dataset generated by the recipient.\n**(V)**\nAny other condition the Director considers appropriate.\n**(B) Standards**\nIn carrying out paragraph (1), the Director shall facilitate the establishment of standards relating to making biological datasets artificial intelligence-ready, in accordance with the definition of artificial intelligence-ready under subparagraph (A)(i)(I).\n**(C) Resources and frameworks**\nIn carrying out paragraph (1), the Director shall facilitate the establishment of data management resources and cybersecurity frameworks for the following:\n**(i)**\nFederal departments and agencies that provide either full or partial Federal funding for research that generates biological datasets.\n**(ii)**\nFederally funded researchers who are collecting, cleaning, curating, or generating biological datasets to make the datasets artificial intelligence-ready.\n**(D) Additional requirements**\nThe Director shall take such actions as may be necessary to ensure the definitions, standards, resources, and frameworks referred to in paragraph (1)\u2014\n**(i)**\nare not overly burdensome on recipients of funding for qualified federally funded research, such that the act of generating biological datasets that are artificial intelligence-ready requires resources and expertise beyond those available to the recipients; and\n**(ii)**\nare tested and evaluated in accordance with subsection (c).\n**(3) Annual updates**\nNot later than 1 year after the date of the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and annually thereafter, the Director shall review such definitions, standards, resources, and frameworks and, as the Director considers appropriate, shall update such definitions, standards, resources, and frameworks in accordance with this section.\n**(4) Consultation**\nTo facilitate the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and any update under paragraph (3), the Director shall carry out the following:\n**(A)**\nAssess any existing standard related to biotechnology or artificial intelligence, including any standards inventoried pursuant to subsection (b)(1)(A), and, if appropriate, facilitate the incorporation of any such standards in the establishment of the standards referred to in paragraph (2)(B).\n**(B)**\nConsult with the following:\n**(i)**\nThe Secretary of Agriculture.\n**(ii)**\nThe Secretary of Defense.\n**(iii)**\nThe Secretary of Energy.\n**(iv)**\nThe Director of the National Aeronautics and Space Administration.\n**(v)**\nThe Director of the National Institutes of Health.\n**(vi)**\nThe Administrator of the National Science Foundation.\n**(vii)**\nThe head of any other Federal department or agency the Director considers appropriate.\n**(C)**\nSeek to consult with the following:\n**(i)**\nPrivate sector entities from the biotechnology industry.\n**(ii)**\nMembers of academia.\n**(5) Personnel**\nTo facilitate the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and any update under paragraph (3), the Director shall hire staff as the Director determines necessary.\n##### (b) Information gathering\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Director shall inventory the following:\n**(A)**\nExisting biotechnology standards utilized by recipients of Federal funding for biotechnology research to generate biological datasets.\n**(B)**\nExisting biological datasets generated by recipients of Federal funding for biotechnology research.\n**(2) Publication**\nNot later than 1 year after the Director completes the inventory requirement under paragraph (1), the Director shall make any information inventoried under that paragraph available to the public through a website of the National Institute of Standards and Technology.\n##### (c) Test and evaluation\nNot later than 2 years after the date of the enactment of this Act, the Director shall coordinate with the Administrator of the National Science Foundation to conduct a test and evaluation of the definitions, standards, resources, and frameworks referred to in subsection (a)(1) on a sample of biological datasets generated as a result of qualified federally funded research to determine the following:\n**(1)**\nWhether such definitions, standards, resources, and frameworks are clearly written, easy to follow, and easily applicable for the generation of biological datasets that are artificial intelligence-ready.\n**(2)**\nWhether compliance with such definitions, standards, resources, and frameworks when generating or curating biological datasets results in an undue burden on the recipients of such qualified federally funded research, and if so, how to modify such definitions, standards, resources, or frameworks, as the case may be, so as to reduce such burden.\n##### (d) Advice and assistance related to Federal department or agency data standards\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the head of a Federal department or agency that provides funding for qualified federally funded research and that seeks to utilize a biological dataset of such department or agency to train an artificial intelligence model may make a request to the Director to provide advice or assistance with respect to developing the following:\n**(A)**\nData standards for such training.\n**(B)**\nAny data management plan related to such data standards.\n**(2) Resources**\nA head of a Federal department or agency that makes a request pursuant to paragraph (1) may enter into an agreement with the Director to provide to the Director any resources as may be necessary for the Director to provide any advice or assistance related to such request.\n**(3) Oversight mechanisms**\nThe Director shall establish the following:\n**(A)**\nA regularly updated central repository, made available to the public as the Director determines appropriate, on which the head of any Federal department or agency may publish any data standards, and data management plan related to such standards, relating to utilizing a biological dataset of such department or agency to train an artificial intelligence model.\n**(B)**\nA publicly available database to serve as a single point of access, updated as the Director determines necessary, on which the head of any Federal department or agency may publish artificial intelligence-ready biological datasets.\n**(C)**\nA mechanism available to each Federal department or agency to make a request pursuant to paragraph (1).\n**(4) Public input**\nThe Director may solicit input and feedback from the public with respect to any advice or assistance related to a request made pursuant to paragraph (1).\n##### (e) Public input and feedback; consultation\nIn carrying out subsection (a)(1), the Director shall carry out the following:\n**(1)**\nSolicit input and feedback from the public regarding the definitions, standards, resources, and frameworks referred to in such subsection.\n**(2)**\nConsult the heads of Federal departments and agencies that provide funding for qualified federally funded research to ensure such departments and agencies are able to develop data standards, and any data management plan associated with such data standards, related to utilizing a biological dataset of such department or agency to train an artificial intelligence model, including the following:\n**(A)**\nThe Secretary of Agriculture.\n**(B)**\nThe Secretary of Defense.\n**(C)**\nThe Secretary of Energy.\n**(D)**\nThe Director of the National Aeronautics and Space Administration.\n**(E)**\nThe Director of the National Institutes of Health.\n**(F)**\nThe Administrator of the National Science Foundation.\n**(G)**\nThe head of any other Federal department or agency as determined by the Director.\n##### (f) Advisory group\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Director shall establish an advisory group to carry out the following:\n**(A)**\nProvide recommendations relating to the definitions, standards, resources, and frameworks referred to in subsection (a)(1).\n**(B)**\nReview and provide feedback with respect to any advice or assistance related to a request made pursuant to subsection (d)(1).\n**(C)**\nProvide recommendations to academic journals for guidelines relating to artificial intelligence-ready biological datasets.\n**(D)**\nSolicit recommendations from the academic community regarding implementation of the definitions, standards, resources, and frameworks.\n**(E)**\nProvide any other guidance the Director may request.\n**(2) Membership**\n**(A) In general**\nThe advisory group established under paragraph (1) shall be composed of not fewer than 12 members. The Director shall carry out the following:\n**(i)**\nAppoint representatives of Federal departments or agencies that award funds to recipients to carry out qualified federally funded research.\n**(ii)**\nSeek to appoint representatives of academia, private sector entities, and academic publishers.\n**(B) Terms**\n**(i) In general**\nEach member shall serve for a term of 2 years.\n**(ii) Renewal**\nSubject to the discretion of the Director, the term of each member may be renewed for an additional 2-year term.\n**(3) Chairperson**\n**(A) Appointment**\nThe Chairperson of the advisory group shall be designated by the Director from among the members.\n**(B) Term**\nThe term of the Chairperson shall be 1 year.\n**(C) Renewal**\nSubject to the discretion of the Director, the term of a Chairperson may be renewed for an additional 1-year term.\n**(4) Reports**\n**(A) Interim report**\nNot later than 1 year after the date of the enactment of this Act, the advisory group shall submit to the Director an interim report that contains advice and guidance with respect to the matters described in paragraph (1).\n**(B) Subsequent reports**\nIf the advisory group or the Director determines appropriate, the advisory group shall submit to the Director subsequent reports relating to the matters described in paragraph (1).\n##### (g) Federal Acquisition Regulation revisions\nThe Federal Acquisition Regulatory Council shall revise the Federal Acquisition Regulation as necessary to implement the definitions, standards, resources, and frameworks established under subsection (a)(1).\n##### (h) Annual report\n**(1) Interim report**\nNot later than 1 year after the date of the enactment of this Act, the Director shall submit to Congress and the Comptroller General of the United States an interim report that includes information relating to the progress of facilitating the establishment of the definitions, standards, resources, and frameworks under subsection (a)(1) and any advice or assistance related to a request made pursuant to subsection (d)(1).\n**(2) Subsequent reports**\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Director shall submit to Congress and the Comptroller General of the United States a report that includes information relating to the following:\n**(A)**\nThe establishment, implementation, and, if applicable, revision, of the definitions, standards, resources, and frameworks referred to in subsection (a)(1).\n**(B)**\nAny advice or assistance related to a request made pursuant to subsection (d)(1).\n**(3) Additional requirement for first subsequent report**\nWith respect to the first subsequent report under paragraph (2), the Director shall include a summary of the testing and evaluation under subsection (c) that includes information relating to the following:\n**(A)**\nThe findings of the testing and evaluation.\n**(B)**\nThe manner by which the Director addressed any concern identified as a result of the testing and evaluation.\n**(C)**\nAn assessment of any burden on recipients of funding for qualified federally funded research regarding ensuring that biological datasets are artificial intelligence-ready.\n**(D)**\nA cost-benefit analysis of the value of ensuring that biological datasets are artificial intelligence-ready in relation to any such burden.\n##### (i) Government Accountability Office report\nNot later than 5 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the impact of the definitions, standards, resources, and frameworks referred to in subsection (a)(1), including the following:\n**(1)**\nAn assessment of the effectiveness of the definitions, standards, resources, and frameworks in ensuring each biological dataset generated by a recipient of funding for qualified federally funded research is artificial intelligent-ready.\n**(2)**\nAn assessment of whether the implementation of the definitions, standards, resources, and frameworks as the case may be, has resulted in an undue burden on any recipient of Federal funding.\n**(3)**\nAny recommendations with respect to the implementation of the definitions, standards, resources, and frameworks.\n##### (j) Sunset\nThis section shall terminate on the date that is 10 years after the date of the enactment of this Act.\n##### (k) Definitions\nIn this section:\n**(1) Biological data**\nThe term biological data means information that is measured, collected, or aggregated for analysis, including associated descriptors, derived from the structure, function, or process of a biological system.\n**(2) Biological dataset**\nThe term biological dataset means a discreet collection of biological data.\n**(3) Biological data repository**\nThe term biological data repository means any centralized data storage capacity meant for managing or storing biological data.",
      "versionDate": "2026-03-12",
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
        "updateDate": "2026-04-02T18:08:59Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7907ih.xml"
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
      "title": "AI-Ready Bio-Data Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-28T04:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI-Ready Bio-Data Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-28T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the National Institute of Standards and Technology to facilitate the establishment of definitions, standards, resources, and frameworks to ensure certain biological datasets are ready for use in artificial intelligence models, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-28T04:48:26Z"
    }
  ]
}
```
