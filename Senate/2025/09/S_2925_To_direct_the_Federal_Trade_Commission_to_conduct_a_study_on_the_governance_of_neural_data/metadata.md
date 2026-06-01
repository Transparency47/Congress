# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2925?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2925
- Title: MIND Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2925
- Origin chamber: Senate
- Introduced date: 2025-09-29
- Update date: 2025-12-16T19:03:57Z
- Update date including text: 2025-12-16T19:03:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-29: Introduced in Senate
- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S6834-3836)
- Latest action: 2025-09-29: Introduced in Senate

## Actions

- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S6834-3836)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-29",
    "latestAction": {
      "actionDate": "2025-09-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2925",
    "number": "2925",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "MIND Act of 2025",
    "type": "S",
    "updateDate": "2025-12-16T19:03:57Z",
    "updateDateIncludingText": "2025-12-16T19:03:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S6834-3836)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-29",
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
          "date": "2025-09-29T21:24:02Z",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "WA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2925is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2925\nIN THE SENATE OF THE UNITED STATES\nSeptember 29, 2025 Mr. Schumer (for himself, Ms. Cantwell , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Federal Trade Commission to conduct a study on the governance of neural data and other related data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Management of Individuals\u2019 Neural Data Act of 2025 or the MIND Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nan individual\u2019s neural data and other related data can be monetized and used to shape individual behavior, emotional states, and decision making in ways existing laws do not adequately address;\n**(2)**\nvertical corporate integration of neurotechnology, artificial intelligence systems, wearable devices, digital platforms, and global data infrastructure may create interconnected systems with insufficient transparency, accountability, or user control regarding the use of such data;\n**(3)**\nsuch concentration increases the risk of behavioral influence, cognitive manipulation, erosion of personal autonomy, and the exacerbation of existing social and economic disparities, particularly in the absence of enforceable privacy protections, including protections of neural data and other related data;\n**(4)**\nthe absence of a comprehensive Federal standard for the collection, processing, and international transfer of such data presents risks to civil liberties and to national security, given the dual-use potential of and foreign interest in the data assets of the United States;\n**(5)**\nstrong protections for such data are essential to safeguard privacy, prevent discrimination and exploitation, and ensure that innovation in neurotechnology applications proceeds with accountability and public trust; and\n**(6)**\nwhile this Act focuses primarily on neural data, related biometric and behavioral data that can reveal mental states may pose similar risks and warrant comparative analysis to identify broader privacy gaps.\n#### 3. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given such term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(4) Neural data**\nThe term neural data means information obtained by measuring the activity of an individual\u2019s central or peripheral nervous system through the use of neurotechnology.\n**(5) Neurotechnology**\nThe term neurotechnology means a device, system, or procedure that accesses, monitors, records, analyzes, predicts, stimulates or alters the nervous system of an individual to understand, influence, restore, or anticipate the structure, activity, or function of the nervous system.\n**(6) Other related data**\nThe term other related data \u2014\n**(A)**\nmeans biometric, physiological, or behavioral information that does not directly measure the neural activity or central or peripheral nervous system of an individual, but can be processed, analyzed, or combined with other data to infer, predict, or reveal cognitive, emotional, or psychological states or neurological conditions; and\n**(B)**\nmay include heart rate variability, eye-tracking patterns, voice analysis, facial expression recognition, sleep patterns, or other signals derived from consumer devices, wearables, or biosensors.\n#### 4. Federal trade commission study and report on neural data governance\n##### (a) Study and report\n**(1) Study**\n**(A) In general**\nThe Commission shall conduct a study on\u2014\n**(i)**\nwhat additional authorities, if any, the Federal Government needs to regulate neural data and other related data that can reveal an individual\u2019s mental state or activity, and to establish appropriate privacy protections for individuals in the United States;\n**(ii)**\nbest practices for privacy and data security for the private sector to protect such data; and\n**(iii)**\nthe extent to which existing laws, regulations, and governing frameworks, including the Health Insurance Portability and Accountability Act of 1996 ( Public Law 104\u2013191 ), govern the use, storage, processing, portability, and privacy of such data, any gaps in law that should be addressed, and potential additional protections for such data that fall outside the scope of such Act.\n**(B) Consultation**\nIn conducting the study described in subparagraph (A), the Commission shall consult with\u2014\n**(i)**\nthe Director of the Office of Science and Technology Policy;\n**(ii)**\nthe Commissioner of Food and Drugs;\n**(iii)**\nother relevant Federal agencies determined appropriate by the Commission; and\n**(iv)**\nrepresentatives of the private sector, academia, civil society, consumer advocacy organizations, labor organizations, patient advocacy organizations, and clinical research stakeholders including medical and health care professionals.\n**(2) Report**\nNot later than 1 year after the date of enactment of this Act, the Commission shall\u2014\n**(A)**\nsubmit to Congress a report on the study conducted under paragraph (1) that\u2014\n**(i)**\nincludes the information described in subsection (b); and\n**(ii)**\ndescribes a regulatory framework that maximizes opportunities for responsible innovation in neurotechnology while minimizing the risks of harm that arise from such innovation, such as discrimination, profiling, surveillance, manipulation, and the misuse of neural data and other related data in employment, healthcare, financial services, education, commerce, and public life; and\n**(B)**\npublish the report on the website of the Commission.\n##### (b) Report contents\nThe report described in subsection (a)(2) shall include\u2014\n**(1)**\nan analysis on\u2014\n**(A)**\nthe collection, processing, storage, sale, and transfer of neural data and other related data; and\n**(B)**\nall relevant uses of neurotechnology, neural data, and other related data for understanding, analyzing, and influencing human mental states and behavior;\n**(2)**\na summary of the ethical, legal, and regulatory landscape surrounding neural data and other related data that can reveal an individual\u2019s mental state or activity, including any existing guidelines related to\u2014\n**(A)**\nthe collection of such data;\n**(B)**\nconsent for the collection, use, and transfer of such data;\n**(C)**\nindividual rights relating to such data;\n**(D)**\npredictive modeling; and\n**(E)**\nusing such data to infer or influence behavior;\n**(3)**\nan assessment of\u2014\n**(A)**\nhow neural and other related data is collected, processed, and transferred in interstate commerce, and the benefits and risks associated with the collection and use of such data, including how such data may serve the public interest, improve the quality of life of the people of the United States, or advance innovation in neurotechnology and neuroscience; and\n**(B)**\nhow the use of such data may pose risks to individuals, including vulnerable populations, across different contexts or use cases;\n**(4)**\nrecommendations for the categorization and oversight of neural data and other related data uses, including\u2014\n**(A)**\na framework that\u2014\n**(i)**\ndistinguishes categories of such data, classifying such data based on both the potential for beneficial use cases (including medical, scientific, or assistive applications), and the potential for individual, societal, or group-level harm arising from misuse;\n**(ii)**\ndescribes the properties of such data based on its capacity to directly or indirectly identify an individual or to reveal or infer sensitive personal information about an individual; and\n**(iii)**\nsuggests corresponding governance requirements such as heightened oversight, stricter consent standards, prohibited use cases regardless of individual consent, enhanced access restrictions, and cybersecurity protections;\n**(B)**\nstandards for computational models of the brain and guidance on assessing harms in contexts where such data is integrated with artificial intelligence or used as part of a system designed to influence behavior or decision making;\n**(C)**\nan analysis of whether, and if so how, individuals may be exposed to unfair, deceptive, or coercive trade practices through the misuse of neural data and other related data across different environments, and recommendations for safeguards to prevent such harms; and\n**(D)**\nrecommendations for categorizing certain applications of neural data and other related data, or certain practices regarding such data, as impermissible, such as those designed to manipulate behavior or erode privacy with respect to an individual\u2019s mental state or activity;\n**(5)**\nan examination of how the application of artificial intelligence to neural and other related data that can reveal an individual\u2019s mental state or activity may reshape the risks, oversight demands, and ethical considerations associated with such data;\n**(6)**\nrecommendations for consumer transparency, consent frameworks, and neural data and other related data use restrictions, such as\u2014\n**(A)**\nlimiting such data use to only clearly disclosed purposes;\n**(B)**\nrestricting the resale of such data to third parties or the use of such data for individual profiling or targeted advertising;\n**(C)**\nthe use of separate, conspicuous consent mechanisms for the use of such data in developing or deploying computational models of the brain;\n**(D)**\nthe public disclosure of\u2014\n**(i)**\nintended uses for such data, sharing practices, and artificial intelligence applications; and\n**(ii)**\npolicies related to the retention and deletion of such data; and\n**(E)**\nprohibited use cases, regardless of individual consent;\n**(7)**\nrecommendations regarding applications of neural data and other related data in specific areas, including\u2014\n**(A)**\nsectors or practices that raise concerns about privacy, manipulation, discrimination, inequality, or long-term harm, such as\u2014\n**(i)**\nemployment practices, such as in hiring, surveillance, or performance evaluation;\n**(ii)**\neducational settings and other settings involving children under the age of 13 and teens;\n**(iii)**\ninsurance, financial, and housing services;\n**(iv)**\nneuromarketing and behavioral shaping, including the targeting of consumers;\n**(v)**\ncommercial surveillance;\n**(vi)**\nmonetization models, such as data brokers, that aggregate or sell neural data and other related data;\n**(vii)**\nthe transfer of neural data and other related data through acquisitions, mergers, or bankruptcy proceedings;\n**(viii)**\nlaw enforcement and the criminal justice system; and\n**(ix)**\nsectors where algorithmic recommendation or design patterns intentionally amplify addictive use or behavioral manipulation;\n**(B)**\nhow existing Federal statutes enforced by the Commission, including the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) and other consumer protection laws, apply to neural data and other related data; and\n**(C)**\nwhether there are regulatory gaps in protecting the privacy of children and teens, including the applicability of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 et seq. ) and related laws to neural data and other related data;\n**(8)**\nan analysis of the potential security risks associated with the collection, use, and transfer of neural data and other related data, including\u2014\n**(A)**\nan assessment of current cybersecurity and data protection requirements applicable to entities that collect, process, or store neural data or other related data, including any gaps in such requirements where such entities fall outside existing Federal standards, such as the Health Insurance Portability and Accountability Act of 1996 ( Public Law 104\u2013191 );\n**(B)**\nan assessment of interagency review models to determine whether certain exports, public releases, or commercial uses of neurotechnologies, including their component parts and integration with artificial intelligence systems, should be subject to restrictions or enhanced controls;\n**(C)**\nan examination of foreign investment risks in neurotechnology firms;\n**(D)**\nrecommendations on actions the Government and nongovernment actors can take to ensure transparency and due diligence in international partnerships involving such data;\n**(E)**\nsupply chain risks involving components used in neurotechnology that are acquired from foreign countries; and\n**(F)**\nthe implications of storing and processing such data locally versus in cloud environments;\n**(9)**\nrecommendations for incentive structures that promote ethical innovation in neurotechnology that prioritize consumer protection and descriptions of how such structures can be aligned with existing regulatory and certification pathways or requirements, such as the development of\u2014\n**(A)**\nvoluntary standards tied to business incentives, such as research and development tax credits and expedited regulatory pathways;\n**(B)**\nfinancial support for responsible scientific inquiry and innovation in neurotechnology, conducted in ethically governed and controlled environments, with safeguards to prevent misuse or harmful applications;\n**(C)**\nregulatory sandbox mechanisms to enable early-stage neural data applications to be tested with agency oversight, informed consent, and structured risk review;\n**(D)**\npolicies that promote long-term support for users of brain-computer interfaces, such as interoperability standards and post-trial maintenance practices;\n**(E)**\ncompetitive incentives, such as procurement preferences for companies that meet specified standards relating to the use of neurotechnology;\n**(F)**\npublic-private partnerships to develop open standards and ethical practices regarding the treatment of neural data and other related data; and\n**(G)**\nways the Centers for Medicare & Medicaid Services and the Food and Drug Administration can coordinate on the use and approval of neurotechnology to reduce reimbursement and coverage barriers;\n**(10)**\na proposed framework for enforcement mechanisms, remedies, and penalties for the misuse of, gross negligence regarding the use of, and unauthorized collection, use, transfer, or disclosure of neural data and other related data; and\n**(11)**\nother analysis and recommendations determined appropriate by the Commission.\n##### (c) Annual updates\nNot later than 1 year after the date the Commission submits the report to Congress under subsection (a), and not less frequently than annually thereafter, the Commission shall publicly update the findings in such report to\u2014\n**(1)**\nreflect evolving advancements in neurotechnology, neural data and other related data use cases, and the associated risks involved with such advancements and use cases; and\n**(2)**\nassess whether additional reports or updates to any guidance are necessary to ensure that privacy, particularly as it relates to neural data and other related data, continues to be protected.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated $10,000,000 for purposes of carrying out this section.\n#### 5. Conditional limitations on Federal agency use of neural data\n##### (a) Guidance to Federal agencies\n**(1) In general**\nNot later than 180 days after the Commission submits the report described in section 4(a)(2), the Director of the Office of Science and Technology Policy, in consultation with the Commission and the Director of the Office of Management and Budget, shall develop guidance, using such report to inform such guidance, regarding the procurement and operational use by Federal agencies of neurotechnology that collects, uses, procures, or otherwise processes neural data or other related data. Such guidance shall identify\u2014\n**(A)**\nprohibited, permissible, and conditionally permitted use cases of such neurotechnology that are consistent with such report;\n**(B)**\ntechnical, procedural, and ethical safeguards regarding each use case of such neurotechnology; and\n**(C)**\nrequirements for transparency, limitations regarding the purposes for which such neurotechnology can be used, individual opt-in consent mechanisms regarding the use of such neurotechnology, and protections for the privacy of the people of the United States.\n**(2) Binding guidance**\nNot later than 60 days after the Director of the Office of Science and Technology Policy develops the guidance under paragraph (1), the Director of the Office of Management and Budget shall issue binding implementation guidance to each Federal agency pursuant to the guidance developed under paragraph (1).\n##### (b) Prohibition\n**(1) In general**\nThe head of a Federal agency may not procure or operate any neurotechnology that collects, uses, procures, or otherwise processes neural data in a manner inconsistent with the guidance issued under subsection (a)(2).\n**(2) Effective date**\nParagraph (1) shall take effect on the date that is 1 year after the date on which the Director of the Office of Management and Budget issues guidance in accordance with subsection (a)(2).",
      "versionDate": "2025-09-29",
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
        "name": "Commerce",
        "updateDate": "2025-12-16T19:03:57Z"
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
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2925is.xml"
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
      "title": "MIND Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MIND Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Management of Individuals\u2019 Neural Data Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Federal Trade Commission to conduct a study on the governance of neural data and other related data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:20Z"
    }
  ]
}
```
