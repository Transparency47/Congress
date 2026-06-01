# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1239?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1239
- Title: Voluntary Sustainable Apparel Labeling Act
- Congress: 119
- Bill type: HR
- Bill number: 1239
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-03-13T13:30:27Z
- Update date including text: 2025-03-13T13:30:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1239",
    "number": "1239",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Voluntary Sustainable Apparel Labeling Act",
    "type": "HR",
    "updateDate": "2025-03-13T13:30:27Z",
    "updateDateIncludingText": "2025-03-13T13:30:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:00:10Z",
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
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1239ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1239\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Mr. Casten (for himself and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Administrator of the Environmental Protection Agency to establish a voluntary sustainable apparel labeling program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Voluntary Sustainable Apparel Labeling Act .\n#### 2. Voluntary sustainable apparel labeling program\n##### (a) In general\n**(1) Establishment**\nThe Administrator of the Environmental Protection Agency (in this section referred to as the Administrator ) shall carry out a voluntary sustainable apparel labeling program (in this section referred to as the labeling program ).\n**(2) Consultation**\nThe Administrator shall establish and operate the labeling program in consultation with the Secretary of Agriculture and the Federal Trade Commission.\n**(3) Regulations**\nNot later than 2 years after the date of enactment of this section, the Administrator shall finalize regulations to carry out the labeling program.\n##### (b) Requirements\nUnder the labeling program\u2014\n**(1)**\nany person that sells an article of apparel may submit an application to the Administrator to enter the article of apparel into the labeling program;\n**(2)**\nthe Administrator shall specify the information to be included in an application under paragraph (1);\n**(3)**\nthe Administrator shall review any application submitted under paragraph (1) and make a determination regarding whether to include the article of apparel in the labeling program\u2014\n**(A)**\non the basis of whether the Administrator believes the person submitting the application will adhere to the requirements of the labeling program; and\n**(B)**\nnot on the basis of an assessment of the benefits to the environment associated with the article of apparel;\n**(4)**\na person (referred to in this section as a participant ) that sells an article of apparel that the Administrator has determined to include in the labeling program (referred to in this section as the participating article of apparel ) may attach a label (referred to in this section as the apparel sustainability label ) to\u2014\n**(A)**\nthe participating article of apparel; or\n**(B)**\npackaging used for the sole purpose of containing the participating article of apparel;\n**(5)**\nthe Administrator shall establish requirements for the visual form of the apparel sustainability label that shall\u2014\n**(A)**\nconvey the information described in paragraph (6) to the consumer in a manner that is determined by the Administrator to be most useful to the consumer at the point of sale in making apparel purchasing decisions;\n**(B)**\nnot convey that any given article of apparel is acceptable or unacceptable, but instead provide the consumer a numerical quantification of the information described in paragraph (6);\n**(C)**\nemploy words, numbers, and imagery, as specified by the Administrator;\n**(D)**\nconvey the fact that the information on the apparel sustainability label has been verified under requirements established by the Environmental Protection Agency; and\n**(E)**\ninclude a logo to help the consumer identify the label as being associated with the labeling program;\n**(6)**\nthe information included on the apparel sustainability label shall\u2014\n**(A)**\nconvey a numerical summary of the best available information regarding the total greenhouse gas emissions released throughout the full life cycle of the participating article of apparel and its input materials, including in association with\u2014\n**(i)**\ngrowing of plant fibers and other agricultural inputs;\n**(ii)**\nmanufacture of the nonagricultural input materials;\n**(iii)**\nmanufacture of the participating article of apparel;\n**(iv)**\npackaging;\n**(v)**\ntransportation of the input materials and the participating article of apparel;\n**(vi)**\nstorage;\n**(vii)**\npresentation in a retail apparel establishment;\n**(viii)**\nconsumer use, including the energy used to\u2014\n**(I)**\nwash the participating article of apparel; and\n**(II)**\nprepare the participating article of apparel for use, including by ironing or pressing;\n**(ix)**\nend-of-life reuse, recycling, treatment, and disposal of the participating article of apparel and its packaging; and\n**(x)**\nany other aspect of the full life cycle of the participating article of apparel associated with greenhouse gas emissions;\n**(B)**\nconvey a summary of the voluntary commitment made regarding the participating article of apparel, as reported under subsection (c)(1); and\n**(C)**\nprovide electronic access immediately available to the consumer at the point of sale through a quick response (QR) code or similar mechanism to additional information relevant to the consumer, which shall include\u2014\n**(i)**\nthe complete information described in subparagraph (A) regarding the participating article of apparel;\n**(ii)**\nthe complete information provided under subsection (c)(1) regarding the participating article of apparel;\n**(iii)**\nthe database established under subsection (d); and\n**(iv)**\nsuch other information as the Administrator determines to be relevant to the consumer;\n**(7)**\nif the participant is the manufacturer of the participating article of apparel, and not the retail establishment selling the participating article of apparel to the end consumer, this fact shall be made clear on the apparel sustainability label;\n**(8)**\nif requested by a participant, the information pertaining to the participating article of apparel that is conveyed under paragraph (6)(A) shall be divided into\u2014\n**(A)**\ninformation identified under clauses (i) through (v) of paragraph (6)(A), for which the participant shall be responsible for reporting; and\n**(B)**\ninformation identified under clauses (vi) through (ix) of paragraph (6)(A), for which the Administrator shall be responsible for estimating on the basis of the typical use of the participating article of apparel;\n**(9)**\nthe distinction between the sources of information referred to in subparagraphs (A) and (B) of paragraph (8) shall be made clear on the apparel sustainability label;\n**(10)**\nno information or imagery shall be included on the apparel sustainability label that has not been specified by the Administrator pursuant to paragraphs (5) and (6);\n**(11)**\nthe Administrator shall establish the method by which the information included on the apparel sustainability label shall be verified, which verification shall\u2014\n**(A)**\nbe conducted in accordance with uniform standards for the collection and analysis of the information for all participating articles of apparel;\n**(B)**\nrequire the use of the best available scientific information;\n**(C)**\nspecify the requirements for entities to be authorized to measure, monitor, verify, and report the information;\n**(D)**\nbe informed by the established international standards for carbon accounting for product life cycle assessment, including\u2014\n**(i)**\nthe ISO 14040 and ISO 14044 standards of the International Organization for Standardization; and\n**(ii)**\nprotocols established under the Greenhouse Gas (GHG) Protocol program of the World Business Council for Sustainable Development and the World Resources Institute, including\u2014\n**(I)**\nthe GHG Protocol for Product Accounting and Reporting; and\n**(II)**\nPublicly Available Specification 2050; and\n**(E)**\nbe informed by and generally align with the current best practices for validating such information in the apparel industry;\n**(12)**\nin establishing the requirements described in paragraphs (5), (6), and (10), the Administrator\u2014\n**(A)**\nshall consult with an expert advisory panel composed of apparel industry stakeholders; and\n**(B)**\nmay consult with such panel either\u2014\n**(i)**\nby establishing a Federal advisory committee under chapter 10 of part I of title 5, United States Code (commonly referred to as the Federal Advisory Committee Act ); or\n**(ii)**\nthrough a negotiated rulemaking under subchapter III of part I of title 5, United States Code (commonly referred to as the Negotiated Rulemaking Act );\n**(13)**\nthe Administrator shall establish a program by which entities shall be certified to perform the activities under paragraph (11)(C);\n**(14)**\nbeginning 7 years after the date of enactment of this Act, and every 5 years thereafter, the Administrator shall\u2014\n**(A)**\npublish a report on the effectiveness, as determined by the Administrator, of the labeling program in achieving objectives, including such effectiveness in\u2014\n**(i)**\nproviding consumers information that consumers find useful; and\n**(ii)**\nreducing the greenhouse gas emissions associated with apparel throughout the full life cycle as described in paragraph (6)(A);\n**(B)**\nreview and revise the regulations under this section to increase such effectiveness, as determined by the Administrator, of the labeling program with respect to the two objectives listed in clauses (i) and (ii) of subparagraph (A); and\n**(C)**\nreport to the Congress any recommendations for amendments to this section that, in the determination of the Administrator, would improve such effectiveness; and\n**(15)**\nthe Administrator shall provide technical assistance, including through consultants, in reporting information as required in accordance with the labeling program, otherwise participating in the labeling program, and reducing greenhouse gas emissions, to\u2014\n**(A)**\nparticipants;\n**(B)**\nentities seeking to become participants; and\n**(C)**\nentities seeking to become certified under paragraph (13).\n##### (c) Voluntary commitments\n**(1) In general**\nThe Administrator shall carry out a program under which a participant may agree to\u2014\n**(A)**\na voluntary commitment to reduce the total greenhouse gas emissions released throughout the full life cycle of participating articles of apparel and their input materials, as described in subsection (b)(6)(A); and\n**(B)**\nmake publicly available, including on the participant\u2019s website, sustainability information pertaining to the participant or the participating article of apparel that is determined by the Administrator to be based on the best available scientific information.\n**(2) Establishment**\nNot later than 2 years after the date of enactment of this Act, the Administrator shall establish the program required by paragraph (1).\n**(3) Encouragement; technical assistance**\nThe Administrator shall encourage participants, and provide technical assistance to participants, to agree to voluntary commitments under this subsection.\n**(4) No mandate**\nThis subsection does not authorize the Administrator to impose any mandate.\n##### (d) Database\nNot later than 2 years after the date of enactment of this Act, the Administrator shall establish a database to provide easy access to consumers and apparel industry stakeholders to information pertaining to the labeling program, including\u2014\n**(1)**\nexplanations of the objectives and the methodologies of the Administrator in establishing the requirements described in subsection (b);\n**(2)**\nthe information described in subsection (b)(6) with respect to each participating article of apparel;\n**(3)**\nthe voluntary commitments of each participant as reported under subsection (c); and\n**(4)**\nany additional available information on the sustainability of apparel that the Administrator determines to be\u2014\n**(A)**\nuseful to the consumer and apparel industry stakeholders; and\n**(B)**\nbased on the best scientifically available information.\n##### (e) Consumer outreach\n**(1) Program**\nNot later than 3 years after the date of enactment of this Act, the Administrator shall establish a program to inform consumers about the labeling program.\n**(2) Requirements**\nThe consumer outreach program established under paragraph (1) shall\u2014\n**(A)**\nprovide retail apparel establishments educational materials and other information to be conveyed to consumers regarding the labeling program;\n**(B)**\nprovide technical assistance to retail apparel establishments regarding the labeling program and the materials and information described in subparagraph (A); and\n**(C)**\nreach the public through a wide range of means, including public service announcements and advertising.\n##### (f) Penalties for fraudulent use of label\n**(1) In general**\nAny person that violates a requirement of this section shall forfeit and pay to the United States a civil penalty of not more than $10,000 for each such violation.\n**(2) Separate violations**\nEach separate violation of a requirement of this section shall be a separate offense, except that in a case of a violation through continuing failure to obey or neglect to obey an order by the Administrator under this section, each day of continuance of such failure or neglect shall be deemed a separate offense.\n**(3) Equitable relief**\nIn a civil action brought under this section, the United States district courts are empowered to grant mandatory injunctions and such other equitable relief as such courts deem appropriate.\n##### (g) Definitions\nIn this section:\n**(1) Apparel industry stakeholders**\nThe term apparel industry stakeholders means\u2014\n**(A)**\nsuppliers and vendors of apparel manufacturers;\n**(B)**\napparel manufacturers;\n**(C)**\nretail apparel establishments;\n**(D)**\nentities that measure, monitor, verify, and report information described under subsection (b)(6);\n**(E)**\ninstitutions of higher education;\n**(F)**\nconsumer organizations; and\n**(G)**\nother experts, as determined by the Administrator.\n**(2) Greenhouse gas**\nThe term greenhouse gas includes each of the following:\n**(A)**\nCarbon dioxide.\n**(B)**\nMethane.\n**(C)**\nNitrous oxide.\n**(D)**\nSulfur hexafluoride.\n**(E)**\nAny hydrofluorocarbon.\n**(F)**\nAny perfluorocarbon.\n**(G)**\nNitrogen trifluoride.\n**(H)**\nAny fully fluorinated linear, branched, or cyclic\u2014\n**(i)**\nalkane;\n**(ii)**\nether;\n**(iii)**\ntertiary amine; or\n**(iv)**\naminoether.\n**(I)**\nAny perfluoropolyether.\n**(J)**\nAny hydrofluoropolyether.\n**(K)**\nAny other fluorocarbon, except for a fluorocarbon with a vapor pressure of less than 1 mm of Hg absolute at 25 degrees Celsius.\n**(3) Greenhouse gas emission**\nThe term greenhouse gas emission means the release of a greenhouse gas into the ambient air.\n**(4) Retail apparel establishment**\nThe term retail apparel establishment means a person that sells an article of apparel to a consumer.",
      "versionDate": "2025-02-12",
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
        "updateDate": "2025-03-13T13:30:27Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1239ih.xml"
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
      "title": "Voluntary Sustainable Apparel Labeling Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T12:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Voluntary Sustainable Apparel Labeling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T12:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Environmental Protection Agency to establish a voluntary sustainable apparel labeling program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T12:48:38Z"
    }
  ]
}
```
