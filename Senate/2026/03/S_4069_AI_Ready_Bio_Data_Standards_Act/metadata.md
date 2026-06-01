# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4069?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4069
- Title: AI-Ready Bio-Data Standards Act
- Congress: 119
- Bill type: S
- Bill number: 4069
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-02T17:59:35Z
- Update date including text: 2026-04-02T17:59:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4069",
    "number": "4069",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "AI-Ready Bio-Data Standards Act",
    "type": "S",
    "updateDate": "2026-04-02T17:59:35Z",
    "updateDateIncludingText": "2026-04-02T17:59:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T15:08:17Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4069is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4069\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Young (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Director of the National Institute of Standards and Technology to establish definitions, standards, resources, and frameworks to ensure certain biological datasets are ready for use in artificial intelligence models, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI-Ready Bio-Data Standards Act .\n#### 2. Definitions, standards, resources, and frameworks by the National Institute of Standards and Technology for certain biological datasets\n##### (a) Establishment\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Director of the National Institute of Standards and Technology (in this section referred to as the Director ), pursuant to recommendations from the advisory group under subsection (f) and taking into account any feedback received under subsection (e), shall establish definitions, standards, resources, and frameworks to ensure each biological dataset generated as a result of qualified federally funded research is artificial intelligence-ready.\n**(2) Requirements for definitions, standards, resources, and frameworks**\n**(A) Definitions**\n**(i) In general**\nIn carrying out paragraph (1), the Director shall establish definitions for the following terms:\n**(I)**\nArtificial intelligence-ready.\n**(II)**\nBiomanufacturing.\n**(III)**\nBiotechnology.\n**(IV)**\nQualified federally funded research.\n**(ii) Requirements for definition of artificial intelligence-ready**\n**(I) In general**\nIn defining artificial intelligence-ready under clause (i)(I), the Director shall develop a definition that, when applied to a biological dataset, requires that the dataset is generated and formatted in a manner that\u2014\n**(aa)**\nenables the effective use of the dataset for training artificial intelligence models; and\n**(bb)**\nsupports advancements in research relating to artificial intelligence and biotechnology.\n**(II) Discretion**\nWith respect to a biological dataset that otherwise meets the definition of artificial intelligence-ready established under clause (i)(I), the Director may, in consultation with the Chief Data Officer of the Federal agency that is responsible for such biological dataset, determine that such dataset is not artificial intelligence-ready.\n**(iii) Requirements for definition of qualified federally funded research**\nIn defining qualified federally funded research under clause (i)(IV), the Director shall include certain conditions that, if satisfied, will result in certain federally funded research being qualified federally funded research. Such conditions shall include the following:\n**(I)**\nThe amount of Federal funding awarded to a recipient.\n**(II)**\nThe capability of the recipient to generate a biological dataset, which may include negative data, that is artificial intelligence-ready, regardless of the ability of the recipient to publish such dataset.\n**(III)**\nThe expertise of the recipient in generating a biological dataset that is artificial intelligence-ready.\n**(IV)**\nThe size of the biological dataset generated by the recipient.\n**(V)**\nAny other condition the Director considers appropriate.\n**(B) Standards**\nIn carrying out paragraph (1), the Director shall establish standards relating to making biological datasets artificial intelligence-ready, in accordance with the definition of artificial intelligence-ready established under subparagraph (A)(i)(I) of this paragraph.\n**(C) Resources and frameworks**\nIn carrying out paragraph (1), the Director shall establish data management resources and cybersecurity frameworks for the following:\n**(i)**\nFederal departments and agencies that provide either full or partial Federal funding for research that generates biological datasets.\n**(ii)**\nFederally funded researchers who are collecting, cleaning, curating, or generating biological datasets to make the datasets artificial intelligence-ready.\n**(D) Additional requirements**\nThe Director shall ensure that the definitions, standards, resources, and frameworks established under paragraph (1)\u2014\n**(i)**\nare not overly burdensome on recipients of funding for qualified federally funded research, such that the act of generating biological datasets that are artificial intelligence-ready requires resources and expertise beyond those available to the recipients; and\n**(ii)**\nare tested and evaluated in accordance with subsection (c) and in consultation with\u2014\n**(I)**\nthe head of any Federal agency the Director considers appropriate;\n**(II)**\nrepresentatives from any private sector entity the Director considers appropriate; and\n**(III)**\nany biotechnology researcher the Director considers appropriate.\n**(3) Annual updates**\nNot later than 1 year after the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and annually thereafter, the Director shall review the definitions, standards, resources, and frameworks and, if the Director considers it appropriate, shall update the definitions, standards, resources, and frameworks in accordance with the requirements of this section.\n**(4) Consultation**\nTo facilitate the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and any update under paragraph (3), the Director shall consult with the following:\n**(A)**\nPrivate sector entities from the biotechnology industry.\n**(B)**\nPrivate sector entities from the frontier artificial intelligence model industry.\n**(C)**\nMembers of academia.\n**(D)**\nThe following heads of Federal agencies that provide funding for qualified federally funded research relating to the generation of biological datasets:\n**(i)**\nThe Secretary of Agriculture.\n**(ii)**\nThe Secretary of Defense.\n**(iii)**\nThe Secretary of Energy.\n**(iv)**\nThe Director of the National Aeronautics and Space Administration.\n**(v)**\nThe Director of the National Institutes of Health.\n**(vi)**\nThe Administrator of the National Science Foundation.\n**(vii)**\nThe head of any other Federal agency the Director considers appropriate.\n**(5) Personnel**\nTo facilitate the establishment of the definitions, standards, resources, and frameworks under paragraph (1), and any update under paragraph (3), the Director shall hire staff as the Director determines necessary.\n##### (b) Information gathering\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Director shall inventory the following:\n**(A)**\nExisting biotechnology standards utilized by recipients of Federal funding for biotechnology research to generate biological datasets.\n**(B)**\nExisting biological datasets generated by recipients of Federal funding for biotechnology research.\n**(2) Publication**\nNot later than 1 year after the Director completes the inventory requirement under paragraph (1), the Director shall make any information inventoried under that paragraph available to the public through a website of the National Institute of Standards and Technology.\n##### (c) Test and evaluation\nNot later than 1 year after the date of the enactment of this Act, and not less frequently than every 2 years thereafter, the Director shall coordinate with the Administrator of the National Science Foundation to conduct a test and evaluation of the definitions, standards, resources, and frameworks established pursuant to subsection (a)(1) on a sample of biological datasets generated as a result of qualified federally funded research to determine the following:\n**(1)**\nWhether the definitions, standards, resources, and frameworks are clearly written, easy to follow, and easily applicable for the generation of biological datasets that are artificial intelligence-ready.\n**(2)**\nWhether compliance with the definitions, standards, resources, and frameworks established under subsection (a)(1) when generating or curating biological datasets results in an undue burden on the recipients of such qualified federally funded research, and if so, how to modify the definitions, standards, resources, and frameworks, as the case may be, so as to reduce the burden.\n##### (d) Agency-Specific data management policies\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act and in accordance with requirements under subsection (e), the Director shall establish or, if already established, review and revise agency-specific data management policies for each Federal agency that provides funding for qualified federally funded research to ensure implementation of policies that require that any biological dataset generated by a recipient of qualified federally funded research is artificial intelligence-ready.\n**(2) Elements**\nThe data management policies described in paragraph (1) shall include the following:\n**(A)**\nA mechanism to ensure sufficient Federal funding to a recipient to satisfy the requirements of the definitions, standards, resources, and frameworks established under subsection (a)(1).\n**(B)**\nA process for the Chief Data Officer of each Federal agency to designate an individual of such agency to ensure compliance with the policies established or revised under paragraph (1).\n**(3) Oversight mechanisms**\nAs part of the agency-specific data management policies under paragraph (1), the Director shall establish the following:\n**(A)**\nA regularly updated central repository of the policies established at each Federal agency, made available to the public as the Director determines appropriate, for the purpose of tracking available policies.\n**(B)**\nA publicly available database to serve as a single point of access, updated as the Director determines necessary, on which the head of any Federal agency may publish artificial intelligence-ready biological datasets.\n**(C)**\nA reporting mechanism available to each Federal agency to report to the Director how the agency is complying with the policies.\n**(D)**\nA mechanism available to each Federal agency to request assistance from the Director regarding compliance with the policies.\n##### (e) Public input and feedback; consultation\nIn establishing the definitions, standards, resources, and frameworks under subsection (a)(1) and the agency-specific data management policies under subsection (d)(1), the Director shall carry out the following:\n**(1)**\nSolicit input and feedback from the public regarding the definitions, standards, resources, and frameworks and the agency-specific data management policies.\n**(2)**\nConsult with the following heads of Federal agencies that provide funding for qualified federally funded research to ensure such agencies are able to comply with the definitions, standards, resources, and frameworks and the agency-specific data management policies:\n**(A)**\nThe Secretary of Agriculture.\n**(B)**\nThe Secretary of Defense.\n**(C)**\nThe Secretary of Energy.\n**(D)**\nThe Director of the National Aeronautics and Space Administration.\n**(E)**\nThe Director of the National Institutes of Health.\n**(F)**\nThe Administrator of the National Science Foundation.\n**(G)**\nThe head of any other Federal agency as determined by the Director.\n##### (f) Advisory group\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Director shall establish an advisory group to carry out the following:\n**(A)**\nTo provide recommendations relating to the definitions, standards, resources, and frameworks established under subsection (a)(1).\n**(B)**\nTo review and provide feedback on the agency-specific data management policies established or revised under subsection (d)(1).\n**(C)**\nTo provide recommendations to academic journals for guidelines relating to artificial intelligence-ready biological datasets.\n**(D)**\nTo solicit recommendations from the academic community regarding implementation of the definitions, standards, resources, and frameworks.\n**(E)**\nTo provide any other guidance the Director may request.\n**(2) Membership**\n**(A) In general**\nThe advisory group established under paragraph (1) shall be composed of not fewer than 12 members to include\u2014\n**(i)**\nrepresentatives of Federal agencies that award funds to recipients to carry out qualified federally funded research; and\n**(ii)**\nrepresentatives of academia, private sector entities, and academic publishers.\n**(B) Terms**\n**(i) In general**\nEach member shall serve for a term of 2 years.\n**(ii) Renewal**\nSubject to the discretion of the Director, the term of each member may be renewed for an additional 2-year term.\n**(3) Chairperson**\n**(A) Appointment**\nThe Chairperson of the advisory group shall be designated by the Director from among the members.\n**(B) Term**\nThe term of the Chairperson shall be 1 year.\n**(C) Renewal**\nSubject to the discretion of the Director, the term of a Chairperson may be renewed for an additional 1-year term.\n**(4) Reports**\n**(A) Interim report**\nNot later than 1 year after the date of the enactment of this Act, the advisory group shall submit to the Director a interim report that contains advice and guidance with respect to the matters described in paragraph (1).\n**(B) Subsequent reports**\nIf the advisory group or the Director determines appropriate, the advisory group shall submit to the Director subsequent reports relating to the matters described in paragraph (1).\n##### (g) Federal Acquisition Regulation revisions\nThe Federal Acquisition Regulatory Council shall revised the Federal Acquisition Regulation as necessary to implement the definitions, standards, resources, and frameworks established under subsection (a)(1).\n##### (h) Annual report\n**(1) Interim report**\nNot later than 1 year after the date of the enactment of this Act, the Director shall submit to Congress and the Comptroller General of the United States an interim report that includes information relating to the progress of establishing the definitions, standards, resources, and frameworks under subsection (a)(1) and the agency-specific data management policies under subsection (d)(1).\n**(2) Subsequent reports**\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter, the Director shall submit to Congress and the Comptroller General of the United States a report that includes information relating to the following:\n**(A)**\nThe establishment, implementation, and, if applicable, revision, of the definitions, standards, resources, and frameworks established under subsection (a)(1).\n**(B)**\nThe establishment, implementation, and, if applicable, revision of the agency-specific data management policies established or revised under subsection (d)(1).\n**(3) Additional requirement for first subsequent report**\nWith respect to the first subsequent report under paragraph (2), the Director shall include a summary of the testing and evaluation under subsection (c) that includes information relating to the following:\n**(A)**\nThe findings of the testing and evaluation.\n**(B)**\nThe manner by which the Director addressed any concern identified as a result of the testing and evaluation.\n**(C)**\nAn assessment of any burden on recipients of funding for qualified federally funded research regarding ensuring that biological datasets are artificial intelligence-ready.\n**(D)**\nA cost-benefit analysis of the value of ensuring that biological datasets are artificial intelligence-ready in relation to any such burden.\n##### (i) Government Accountability Office report\nNot later than 5 years after the date of the enactment of this Act, the Comptroller General of the United States shall submit to Congress a report on the impact of the definitions, standards, resources, and frameworks established under subsection (a)(1), including the following:\n**(1)**\nAn assessment of the effectiveness of the definitions, standards, resources, and frameworks in ensuring each biological dataset generated by a recipient of funding for qualified federally funded research is artificial intelligence-ready.\n**(2)**\nAn assessment of whether the implementation of the definitions, standards, resources, and frameworks, as the case may be, has resulted in an undue burden on any recipient of Federal funding.\n**(3)**\nAny recommendations with respect to the implementation of the definitions, standards, resources, and frameworks.\n##### (j) Sunset\nThis section shall terminate on the date that is 10 years after the date of the enactment of this Act.\n##### (k) Definitions\nIn this section:\n**(1) Biological data**\nThe term biological data means information that is measured, collected, or aggregated for analysis, including associated descriptors, derived from the structure, function, or process of a biological system.\n**(2) Biological dataset**\nThe term biological dataset means a discreet collection of biological data.\n**(3) Biological data repository**\nThe term biological data repository means any centralized data storage capacity meant for managing or storing biological data.\n**(4) Negative data**\nThe term negative data means data that disproves, fails to support, or explains through previously unknown or contradictory means a research hypothesis but that otherwise still advances scientific knowledge or understanding.",
      "versionDate": "2026-03-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-04-02T17:59:35Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4069is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Director of the National Institute of Standards and Technology to establish definitions, standards, resources, and frameworks to ensure certain biological datasets are ready for use in artificial intelligence models, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T05:18:30Z"
    },
    {
      "title": "AI-Ready Bio-Data Standards Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI-Ready Bio-Data Standards Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T05:08:19Z"
    }
  ]
}
```
