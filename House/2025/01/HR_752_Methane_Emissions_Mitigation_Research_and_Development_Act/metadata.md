# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/752?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/752
- Title: Methane Emissions Mitigation Research and Development Act
- Congress: 119
- Bill type: HR
- Bill number: 752
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2026-02-27T09:06:50Z
- Update date including text: 2026-02-27T09:06:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/752",
    "number": "752",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
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
    "title": "Methane Emissions Mitigation Research and Development Act",
    "type": "HR",
    "updateDate": "2026-02-27T09:06:50Z",
    "updateDateIncludingText": "2026-02-27T09:06:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:03:45Z",
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
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "OR"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr752ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 752\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Casten introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo provide for methane emission detection and mitigation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Methane Emissions Mitigation Research and Development Act .\n#### 2. Methane emission detection and mitigation\n##### (a) In general\nSubtitle F of title IX of the Energy Policy Act of 2005 ( 42 U.S.C. 16291 et seq. ) is amended by adding at the end the following new section:\n969E. Methane leak detection and mitigation (a) Technical assistance (1) In general The Secretary, in consultation with the Administrator of the Environmental Protection Agency, the Secretary of Commerce, and the heads of other appropriate Federal agencies, shall carry out a program of methane emissions detection and mitigation research, development, and demonstration for technologies and methods that significantly detect, quantify, and mitigate methane emissions. In carrying out the program, the Secretary shall\u2014 (A) enter into cooperative agreements with State or local governments, institutions of higher education, or for-profit entities to provide technical assistance to\u2014 (i) prevent or respond to methane releases, including prediction, detection, mitigation, quantification, and identification of leaks, vents, and other outflows throughout the natural gas infrastructure (including natural gas storage, pipelines, and natural gas production sites); and (ii) protect public health in the event of a major methane release; (B) in coordination with representatives from private sector entities, State and local governments, and institutions of higher education, establish a publicly accessible resource for best practices in the design, construction, maintenance, performance, monitoring, and incident response for\u2014 (i) pipeline systems, including compressor stations; (ii) production wells; (iii) storage facilities; and (iv) other vulnerable infrastructure; (C) in coordination with representatives from private sector entities, State and local governments, and institutions of higher education, establish a publicly accessible resource for best practices in evaluation and incorporation of emission reduction technologies, including\u2014 (i) metrics for performance evaluation; and (ii) principles for selection and integration of emission reduction technologies that are best suited for the project or entity concerned; (D) support research of technologies to more accurately quantify emissions, including\u2014 (i) the ability to accurately characterize and measure methane emissions through various atmospheric conditions such as wind, rain, fog, and dust; (ii) improvements to data analytics and machine learning platforms; (iii) the ability to characterize temporal patterns in emissions, such as through continuous monitoring or multitiered system practices; (iv) improvements to high-resolution spectroscopic databases of methane; (v) the ability to remotely detect carbon and ethane isotopes to facilitate attribution of sources of methane emissions; and (vi) improvements to Lidar detection technologies; (E) identify high-risk characteristics of pipelines, wells, storage facilities, and materials, geologic risk factors, or other key factors that increase the likelihood or intensity of methane emissions leaks; (F) identify methane mitigation methods and technologies in coal mines; and (G) in collaboration with private sector entities and institutions of higher education, quantify and map significant geologic methane seeps and other sources of natural emissions across the United States. (2) Considerations In carrying out the program under this section, the Secretary shall consider the following: (A) Historical data of methane emissions. (B) Public health consequences. (C) Public safety. (D) Novel materials and designs for pipelines, compressor stations, components, and wells (including casing, cement, and wellhead). (E) Regional geologic traits. (F) Induced and natural seismicity. (b) Methane leak detection consortium (1) In general Not later than 1 year after the date of the enactment of this section, the Secretary shall establish and operate a Methane Emissions Measurement and Mitigation Research Consortium (in this section referred to as the Consortium ) for the purpose of supporting, to the maximum extent practicable, data sharing, research prioritization, and researching cooperative leak detection and repair strategies pertaining to methane emissions detection, quantification, and mitigation. (2) Membership The members of the Consortium shall be representatives from the National Institute of Standards and Technology, other relevant Federal agencies, National Laboratories, oil and gas operators and industry groups, vendors of methane detection and quantification technologies, institutions of higher education, community organizations, relevant nongovernmental organizations, and other entities. (3) Responsibilities The Consortium shall develop and implement a multiyear plan that\u2014 (A) identifies technical goals and milestones for the Consortium; and (B) facilitates data sharing for the purposes of\u2014 (i) bettering the understanding of methane emissions from the oil and gas sector; (ii) improving emissions detection, measurement, and mitigation capabilities, including assessing multi-tiered atmospheric measurements; and (iii) improving the understanding of methane quantification data analytics and machine learning platforms, including for calibration of measurements. (4) Reporting (A) In general The Secretary shall report on the Consortium\u2019s activities to the appropriate congressional committees. (B) Initial report Not later than 18 months after the date of the enactment of this section, the Secretary shall submit to the appropriate congressional committees a report summarizing the activities, findings, and progress of the program under this section. The report shall include the following: (i) A review of LDAR technologies available to the oil and gas sector for the purpose of methane emissions measurement and mitigation. (ii) A summary of research gaps and priorities related to methane emissions detection, measurement, and mitigation capabilities. (iii) A description of the data sharing and cooperative activities that have been initiated pursuant to paragraph (3)(B). (C) Annual report Not later than 1 year after the date on which the report under subparagraph (B) is submitted and annually thereafter, the Secretary shall submit to the appropriate congressional committees a report summarizing the activities, findings, and progress of the program under this section. The report shall include the following: (i) An updated review of LDAR technologies available to oil and gas operators for the purpose of methane emissions measurement and mitigation. (ii) A description of the state of methane emissions detection and measurement capabilities. (iii) A summary of research priorities relating to methane emissions detection, measurement, and mitigation. (iv) An update on the data sharing and cooperative activities undertaken by members of the Consortium. (5) Sunset; termination (A) In general The Secretary may provide support to the Consortium for a period of not more than ten years, subject to the availability of appropriations. (B) Merit review Not later than 5 years after the date on which the Consortium is established, the Secretary shall conduct a review to determine whether the Consortium has achieved the technical goals and milestones identified under paragraph (3)(A). (6) Definitions In this section: (A) Appropriate congressional committees The term appropriate congressional committees means the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Energy and Natural Resources of the Senate. (B) LDAR The term LDAR means a technology, program, or activity that is intended to monitor, detect, measure, or repair methane leaks. (C) Secretary The term Secretary means the Secretary of Energy. (7) Authorization of appropriations There are authorized to be appropriated to the Secretary to carry out this section the following: (A) $36,000,000 for fiscal year 2026. (B) $38,000,000 for fiscal year 2027. (C) $40,000,000 for fiscal year 2028. (D) $42,000,000 for fiscal year 2029. (E) $44,000,000 for fiscal year 2030. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Energy Policy Act of 2005 is amended by adding at the end of the items relating to subtitle F of title IX of such Act the following new item:\nSec. 969E. Methane leak detection and mitigation. .\n##### (c) National facilities for testing and intercalibration program relating to methane\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act and subject to the availability of appropriations, the Secretary of Commerce, in consultation with the Secretary of Energy and the Administrator of the Environmental Protection Agency, shall establish a program through the National Institute of Standards and Technology\u2019s Center for Greenhouse Gas Measurements, Standards, and Information established pursuant to section 10222 of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 42 U.S.C. 18932 ) that establishes national facilities to advance methane detection, quantification, and relevant standards and supporting methods for testing and intercalibration of methane measurements and the publication and maintenance of standards for such measurements.\n**(2) Responsibilities**\nThe facilities established under paragraph (1) shall facilitate detection and quantification of carbon, carbon isotopes, methane, ethane, and gases associated with such sources, provide high-resolution spectroscopic reference data advancing accuracy of remote sensing technologies, develop methods relating methane concentration observations to the associated emission fluxes, and facilitate the rapid performance testing of existing and new technologies for the measurement of methane emissions, including testing conditions with a wide range of the following:\n**(A)**\nSizes and extents of emission sources.\n**(B)**\nGeographic diversity.\n**(C)**\nTemporal characteristics.\n**(D)**\nDiversity of atmospheric conditions, such as wind, rain, fog, clouds, and dust.\n**(E)**\nDiversity of observing platforms.\n**(F)**\nQuantification of atmospheric emission plumes.\n**(3) Annual report**\nNot later than 2 years after the date of the enactment of this Act and annually thereafter, the Secretary of Commerce shall submit to Congress a report summarizing the activities, findings, and progress of the program established under paragraph (1).\n**(4) Authorization of appropriations**\nThere are authorized to be appropriated to the Secretary of Commerce to carry out this section the following:\n**(A)**\n$15,000,000 for fiscal year 2026.\n**(B)**\n$17,000,000 for fiscal year 2027.\n**(C)**\n$19,000,000 for fiscal year 2028.\n**(D)**\n$21,000,000 for fiscal year 2029.\n**(E)**\n$23,000,000 for fiscal year 2030 and each fiscal year thereafter.",
      "versionDate": "2025-01-28",
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
        "name": "Energy",
        "updateDate": "2025-03-01T15:50:41Z"
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
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr752ih.xml"
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
      "title": "Methane Emissions Mitigation Research and Development Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T11:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Methane Emissions Mitigation Research and Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for methane emission detection and mitigation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T11:18:29Z"
    }
  ]
}
```
