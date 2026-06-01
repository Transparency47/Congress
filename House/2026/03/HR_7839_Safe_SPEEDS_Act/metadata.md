# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7839?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7839
- Title: Safe SPEEDS Act
- Congress: 119
- Bill type: HR
- Bill number: 7839
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-03-27T21:57:08Z
- Update date including text: 2026-03-27T21:57:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7839",
    "number": "7839",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001241",
        "district": "47",
        "firstName": "Dave",
        "fullName": "Rep. Min, Dave [D-CA-47]",
        "lastName": "Min",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Safe SPEEDS Act",
    "type": "HR",
    "updateDate": "2026-03-27T21:57:08Z",
    "updateDateIncludingText": "2026-03-27T21:57:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:04:35Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-16",
      "state": "PA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-16",
      "state": "NY"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-03-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7839ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7839\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Mr. Min (for himself, Mr. Lawler , and Mr. Huffman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Consumer Product Safety Commission to promulgate a consumer product safety standard for the uniform classification and labeling of certain electric bicycles and other off-road electric devices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Standards for Personal E-bike and E-moto Device Specifications Act or the Safe SPEEDS Act .\n#### 2. Consumer product safety standard for low-speed electric bicycles and other off-road electric devices\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Commission shall promulgate, under section 553 of title 5, United States Code, a final consumer product safety standard for the uniform classification and labeling of low-speed electric bicycles and other off-road electric devices that are manufactured in, offered for sale to a consumer in, or imported into the United States.\n##### (b) Analysis; consultation; evaluation\nThe Commission shall carry out the following:\n**(1)**\nTo the extent feasible, conduct and publish an analysis with respect to any crash, injury, and fatality associated with the use of a low-speed electric bicycle or any other off-road electric device reported during the 5-year period that precedes the date of the enactment of this Act, disaggregated by\u2014\n**(A)**\nthe age of the user of the bicycle or device; and\n**(B)**\nthe type of bicycle or device, including\u2014\n**(i)**\nwhether the bicycle or device involved in the crash, injury, or fatality is a low-speed electric bicycle, any other off-road electric device described in subsection (h)(7)(A), or another bicycle or device; and\n**(ii)**\nif the bicycle or device is a low-speed electric bicycle, the classification of the bicycle as a class 1 electric bicycle, class 2 electric bicycle, class 3 electric bicycle (as defined in section 217(j)(2) of title 23, United States Code), or as none of such classifications.\n**(2)**\nEvaluate the efficacy of Federal, State, and local laws, regulatory guidance, industry best practices, and international standards related to classifying, labeling, and establishing age restrictions for low-speed electric bicycles and other off-road electric devices (including the classifications of class 1 electric bicycle, class 2 electric bicycle, or class 3 electric bicycle as defined in section 217(j)(2) of title 23, United States Code) to determine whether the Commission should consider any such law, regulatory guidance, or best practice in carrying out the requirements described in subsection (c).\n**(3)**\nTo the extent feasible and appropriate, consult with the following:\n**(A)**\nManufacturers, importers, and sellers of low-speed electric bicycles and other off-road electric devices.\n**(B)**\nIndependent product safety engineers and experts.\n**(C)**\nRepresentatives of consumer and transportation safety advocacy groups.\n**(D)**\nThe National Highway Traffic Safety Administration.\n**(E)**\nAny other entity as the Commission determines appropriate.\n##### (c) Requirements\nBased on the analysis, evaluation, and consultation required under subsection (b), the Commission shall ensure the standard promulgated under subsection (a) includes the following:\n**(1)**\nDefinitions of distinct classifications for low-speed electric bicycles and other off-road electric devices.\n**(2)**\nMinimum age recommendations for the use of low-speed electric bicycles and other off-road electric devices with respect to each classification defined pursuant to paragraph (1).\n**(3)**\nA requirement that a low-speed electric bicycle or any other off-road electric device\u2014\n**(A)**\nsatisfies a classification defined pursuant to paragraph (1); and\n**(B)**\nincludes, at the time a low-speed electric bicycle or any other off-road electric device is offered for sale, a permanent, clearly visible, and consistently placed label on such bicycle or device that specifies\u2014\n**(i)**\nthe classification satisfied;\n**(ii)**\nthe motor power of the bicycle or device;\n**(iii)**\nthe maximum speed of the bicycle or device when powered solely by a motor;\n**(iv)**\nthe relevant minimum age recommendation described in paragraph (2); and\n**(v)**\nwith respect to any other off-road electric device described in subsection (h)(7)(A), any such device\u2014\n**(I)**\nis not intended for on-road use; and\n**(II)**\ndoes not satisfy any motor vehicle safety standard prescribed under chapter 301 of title 49, United States Code.\n**(4)**\nA prohibition on the sale, offer for sale to a consumer, or display of a consumer product labeled as a low-speed electric bicycle that\u2014\n**(A)**\ndoes not satisfy the definition of a low-speed electric bicycle;\n**(B)**\nis designed, manufactured, or displayed by the manufacturer, importer, or seller of the consumer product to have the capacity to be configured or modified to increase the maximum speed or motor power of the consumer product such that the consumer product would no longer satisfy such definition; or\n**(C)**\nis designed, manufactured, or displayed by the manufacturer, importer, or seller for off-road use and does not have operable pedals.\n##### (d) Modifications\nAt any time after the promulgation of the standard under subsection (a), the Commission may, through a rulemaking under section 553 of title 5, United States Code, modify the requirements of the standard.\n##### (e) Treatment of standard\nA standard promulgated under this section, including a modification of such standard, shall be treated as a consumer product safety rule promulgated under section 9 of the Consumer Product Safety Act ( 15 U.S.C. 2058 ).\n##### (f) Analysis on crashes, injuries, and fatalities\n**(1) In general**\nNot later than 2 years after the promulgation of the standard under subsection (a), and periodically thereafter at regular intervals, the Commission shall conduct an analysis of any crash, injury, and fatality associated with the use of a low-speed electric bicycle or any other off-road electric device reported beginning on the date of the enactment of this Act or on the date of the publication of the most recent analysis conducted under this paragraph, whichever date is later, disaggregated by\u2014\n**(A)**\nthe age of the user of the bicycle or device; and\n**(B)**\nthe type of bicycle or device, including\u2014\n**(i)**\nwhether the bicycle or device involved in the crash, injury, or fatality is\u2014\n**(I)**\na low-speed electric bicycle;\n**(II)**\nany other off-road electric device described in subsection (h)(7)(A); or\n**(III)**\na bicycle or device that\u2014\n**(aa)**\ndoes not satisfy\u2014\n(AA)\na classification defined pursuant to subsection (c)(1); or\n(BB)\na requirement described in subsection (c)(3); or\n**(bb)**\nviolates the prohibition described in subsection (c)(4); and\n**(ii)**\nthe classification defined pursuant to subsection (c)(1) that each such bicycle or device satisfies.\n**(2) Consultation**\nThe Commission shall consult with a relevant entity and any other entity as the Commission determines feasible and appropriate to conduct any study required by paragraph (1).\n**(3) Redundancy**\nIn conducting any study required by paragraph (1), the Commission shall avoid duplicating information to the fullest extent practicable.\n**(4) Report; publication**\nNot later than 30 days after the date on which any study required by paragraph (1) is completed, the Commission shall\u2014\n**(A)**\nsubmit to Congress a report on the findings of the study; and\n**(B)**\npublish the study on a website of the Commission in a publicly accessible format.\n##### (g) Grants; training module\n**(1) Grants**\n**(A) In general**\nFor each of fiscal years 2027 through 2031, the Commission shall award grants to relevant entities to carry out the following:\n**(i)**\nHire and train personnel to ensure sufficient capacity and expertise for data collection, reporting, and recordkeeping related to any crash, injury, or fatality associated with low-speed electric bicycles and other off-road electric devices, including for the identification and classification of such bicycles pursuant to the classifications defined pursuant to subsection (c)(1).\n**(ii)**\nDevelop and implement\u2014\n**(I)**\npolicies, guidance, or best practices to assist with the compliance or enforcement of this Act in relation to other applicable Federal, State, and local laws, including policies, guidance, or best practices for manufacturers, importers, or sellers of low-speed electric bicycles and other off-road electric devices;\n**(II)**\ndata collection and reporting protocols to enable the standardization, accuracy, and comprehensiveness of data on any crash, injury, or fatality associated with low-speed electric bicycles and other off-road electric devices; and\n**(III)**\npublic education and safety initiatives to improve awareness of safety risks associated with the use of low-speed electric bicycles and other off-road electric devices, including education and initiatives related the standard promulgated under subsection (a) and the requirements described in subsection (c).\n**(iii)**\nAny other purpose the Commission determines necessary to support any study required by subsection (f)(1).\n**(B) Authorization of Appropriations**\nThere is authorized to be appropriated to the Commission $2,500,000 for each of fiscal years 2027 through 2031 to award grants under this subsection.\n**(2) Training Module**\nThe Commission shall develop a publicly accessible training module to\u2014\n**(A)**\ninstruct relevant entities on how to identify and classify a low-speed electric bicycle and any other off-road electric device based on the standard promulgated under subsection (a); and\n**(B)**\nimprove the standardization, accuracy, and comprehensiveness of data collection and reporting with respect to any crash, injury, or fatality associated with such bicycles and devices.\n##### (h) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Consumer Product Safety Commission.\n**(2) Consumer product**\nThe term consumer product has the meaning given the term in section 3 of the Consumer Product Safety Act ( 15 U.S.C. 2052 ).\n**(3) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(4) Local government**\nThe term local government means any unit of government within a State, including the following:\n**(A)**\nA city.\n**(B)**\nA town.\n**(C)**\nA county.\n**(D)**\nA municipality.\n**(E)**\nA special district.\n**(F)**\nA school district.\n**(G)**\nAny other agency or instrumentality of a State or local government.\n**(5) Low-speed electric bicycle**\nThe term low-speed electric bicycle has the meaning given the term in section 38 of the Consumer Product Safety Act ( 15 U.S.C. 2085 ).\n**(6) Native Hawaiian organization**\nThe term Native Hawaiian organization \u2014\n**(A)**\nmeans an organization that\u2014\n**(i)**\nserves and represents the interests of Native Hawaiians;\n**(ii)**\nprovides services to Native Hawaiians; and\n**(iii)**\nhas expertise in Native Hawaiian affairs; and\n**(B)**\nincludes Native Hawaiian organizations registered with Office of Native Hawaiian Relations of the Department of the Interior.\n**(7) Other off-road electric device**\nThe term other off-road electric device means\u2014\n**(A)**\na consumer product that\u2014\n**(i)**\nis designed, manufactured, or recommended by the manufacturer, importer, or seller for off-road use;\n**(ii)**\nis powered by an electric motor;\n**(iii)**\nmay or may not have operable pedals; and\n**(iv)**\nis equipped with\u2014\n**(I)**\nfewer than 4 wheels;\n**(II)**\na seat or saddle designed to be straddled by the user of the consumer product; and\n**(III)**\nhandlebars for steering control of the user; or\n**(B)**\nany other consumer product as determined by the Commission.\n**(8) Relevant entity**\nThe term relevant entity means any of the following:\n**(A)**\nA law enforcement agency.\n**(B)**\nAn emergency management service agency that is\u2014\n**(i)**\noperated by a State, local, or Tribal government or Native Hawaiian organization; or\n**(ii)**\ndescribed in section 501(c) of title 26, United States Code.\n**(C)**\nA State.\n**(D)**\nA local government.\n**(E)**\nA Tribal government.\n**(F)**\nA Native Hawaiian organization.\n**(9) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, Guam, the Commonwealth of the Northern Mariana Islands, the Virgin Islands of the United States, and any other territory or possession of the United States.\n**(10) Tribal government**\nThe term Tribal government means the recognized governing body of an Indian Tribe.",
      "versionDate": "2026-03-05",
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
        "name": "Commerce",
        "updateDate": "2026-03-27T21:57:08Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7839ih.xml"
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
      "title": "Safe SPEEDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T04:58:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe SPEEDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Standards for Personal E-bike and E-moto Device Specifications Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Consumer Product Safety Commission to promulgate a consumer product safety standard for the uniform classification and labeling of certain electric bicycles and other off-road electric devices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T04:48:31Z"
    }
  ]
}
```
