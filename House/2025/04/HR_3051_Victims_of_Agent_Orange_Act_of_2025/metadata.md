# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3051?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3051
- Title: Victims of Agent Orange Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3051
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2026-02-21T09:05:58Z
- Update date including text: 2026-02-21T09:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-28 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3051",
    "number": "3051",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Victims of Agent Orange Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:58Z",
    "updateDateIncludingText": "2026-02-21T09:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-28T16:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "IN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "DE"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "MA"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CT"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "TX"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "IL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "TN"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3051ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3051\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Ms. Tlaib (for herself, Ms. Simon , Mr. Nadler , Mr. Thanedar , Mr. Carson , and Ms. McBride ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Administrator of the United States Agency for International Development, or its successor, and the Secretary of Health and Human Services to provide assistance for individuals affected by exposure to Agent Orange, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Victims of Agent Orange Act of 2025 .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nFrom 1961 to 1971, approximately 19,000,000 gallons of 15 different herbicides were sprayed over the southern region of Vietnam by the United States military.\n**(2)**\nThe herbicides included 13,000,000 gallons of Agent Orange, 4,500,000 gallons of Agent White, 1,000,000 gallons of Agent Blue, 420,000 gallons of Agent Purple, and relatively smaller quantities of the other herbicides. Many of the herbicides, including Agents Orange, Purple, Green, Pink, Dinoxol, and Trinoxol, contained the toxic contaminant dioxin (TCDD). Agent Blue contained high levels of arsenic. The 15 herbicides, including the contaminant dioxin, are usually collectively referred to as Agent Orange.\n**(3)**\nBetween 1961 and 1971, nearly 20,000 spraying missions were carried out in an area of about 12,600,000 hectares. This represented about 12 percent of South Vietnam and portions of Laos and Cambodia. These amounts only account for the United States Air Force Operation Ranch Hand spraying and do not include the widespread use of Agent Orange by the Army Chemical Corps, Central Intelligence Agency, and South Vietnamese Government.\n**(4)**\nStudies have found that between 2,100,000 and 4,800,000 Vietnamese, Lao, and Cambodian people and tens of thousands of Americans were exposed to Agent Orange during the spraying operations. Many other Vietnamese people were or continue to be exposed to Agent Orange through contact with the environment and food that was contaminated. Many offspring of those who were exposed have birth defects, developmental disabilities, and other diseases.\n**(5)**\nToday, there are still dozens of herbicide hotspots that continue to contaminate the food, soil, sediment, livestock, and wildlife with Agent Orange. Concentrations of TCDD as high as 1,000 mg/kg have been found in soil and sediment samples more than 50 years after Agent Orange was sprayed in Vietnam.\n**(6)**\nSince 2007, the United States has provided assistance to Vietnam in remediating Agent Orange contamination at the largest of these hotspots, which are the airbases that handled the spray missions. The contamination at the Da Nang Airport has been fully cleaned up, and the United States has committed funds to contribute to cleaning up the Bien Hoa Airbase, which has the most wide-spread herbicide contamination in Vietnam. There are at least two dozen other smaller hotspots scattered throughout southern and central Vietnam that also must be remediated, since they continue to expose local populations to dioxin and arsenic.\n**(7)**\nAgent Orange exposure continues to negatively affect the lives of veterans of the United States Armed Forces, Vietnamese people, Vietnamese Americans, and their children. The lives of many victims are cut short, and others live with disease, disabilities, and pain, which are often untreated or unrecognized.\n**(8)**\nThe Department of Veterans Affairs recognizes 19 illnesses and diseases, including AL amyloidosis, bladder cancer, chronic B- cell leukemia, chloracne, diabetes mellitus type 2, high blood pressure (hypertension), Hodgkin\u2019s disease, hypothyroidism, ischemic heart disease, monoclonal gammopathy of undetermined significance (MGUS), multiple myeloma, non-Hodgkin\u2019s Lymphoma, Parkinson\u2019s disease, Parkinsonism, acute and sub-acute peripheral neuropathy, porphyria cutanea tarda, prostate cancer, respiratory cancers, and soft-tissue sarcomas associated with the spraying and use of Agent Orange by the United States Armed Forces during the Vietnam era.\n**(9)**\nNo similar recognition has been given to affected Vietnamese or Vietnamese Americans.\n**(10)**\nThe Department of Veterans Affairs provides compensation for many severe birth defects among the children of United States women veterans who served in Vietnam. The list of birth defects covered includes, but is not limited to, achondroplasia, cleft lip, cleft palate, congenital heart disease, congenital talipes equinovarus (clubfoot), esophageal and intestinal atresia, Hallerman-Streiff syndrome, hip dysplasia, Hirschsprung\u2019s disease (congenital megacolon), hydrocephalus due to aqueductal stenosis, hypospadias, imperforate anus, neural tube defects, Poland syndrome, pyloric stenosis, syndactyly (fused digits), tracheoesophageal fistula, undescended testes, and Williams syndrome. Affected children of these women veterans receive medical care and other benefits. However, the care and compensation provided by the Department of Veterans Affairs to the covered children of United States veterans is insufficient to meet their needs related to Agent Orange.\n**(11)**\nThe only birth defect recognized for the children of male American veterans is spina bifida (but not occulta). However, many children of male Vietnam war veterans have the same range of birth defects and diseases as seen in the children of female Vietnam war veterans. This discrepancy results in most Agent Orange affected children of United States veterans receiving no care or benefits.\n**(12)**\nNo assistance has been given to the children of male or female Vietnamese or Vietnamese Americans connected with their exposure, or their parents\u2019 or grandparents\u2019 exposure.\n**(13)**\nThe Institute of Medicine for the past several years has noted that it is considerably more plausible than previously believed that exposure to the herbicides sprayed in Vietnam might have caused paternally mediated transgenerational effects attributable to the TCCD contaminant in Agent Orange . In recent years, scientific studies have identified likely epigenetic links between exposure to toxins and birth defects and developmental disorders in subsequent generations. Some of the children and grandchildren of exposed persons (Americans, Vietnamese, and Vietnamese Americans) who were in southern Vietnam during the Vietnam war era likely suffer from disorders, birth defects, and illnesses related to Agent Orange.\n**(14)**\nThe assistance that the United States has provided for environmental remediation of contamination at the Da Nang and Bien Hoa airports has, in recent years, included funds for public health and disabilities activities for individuals residing in some affected areas.\n**(15)**\nLaos and Cambodia were also sprayed with Agent Orange during the Vietnam war era. At least 527,000 gallons of Agent Orange were sprayed in Laos and significant amounts were also sprayed in Cambodia. Affected Lao and Cambodian people over several generations suffer from medical conditions, birth defects, and disabilities similar to those seen in Vietnam and the United States. The United States has the responsibility to take action to mitigate and provide compensation for those effects. Further action will be needed to ascertain and effectively address this legacy of the Vietnam war.\n##### (b) Purpose\nIt is the purpose of this Act to address and remediate the ongoing damage that arose or will continue to arise from the use of Agent Orange during the Vietnam war.\n#### 3. Assistance for individuals affected by health issues related to exposure to Agent Orange\n##### (a) For covered individuals\nThe Administrator of the United States Agency for International Development, or its successor, in coordination with the heads of other appropriate Federal agencies and nongovernmental organizations, shall provide assistance to address the health care needs of covered individuals. Such assistance may include the provision of medical and chronic care services, nursing services, vocational employment training, and medical equipment.\n##### (b) For caregivers\nThe Administrator of the United States Agency for International Development, or its successor, in coordination with the heads of other appropriate Federal agencies and nongovernmental organizations, shall provide assistance to institutions in Vietnam that provide health care for covered individuals. Such assistance may include\u2014\n**(1)**\nmedicines and medical equipment;\n**(2)**\ncustodial care, home care, respite care, and daycare programs;\n**(3)**\ntraining programs for caregivers;\n**(4)**\nmedical and physical rehabilitation, and counseling services and equipment for illnesses and deformities associated with exposure to Agent Orange; and\n**(5)**\nreconstructive surgical programs.\n##### (c) For housing and poverty reduction\nThe Administrator of the United States Agency for International Development, or its successor, in coordination with the heads of other appropriate Federal agencies and nongovernmental organizations shall provide\u2014\n**(1)**\nassistance to institutions in Vietnam that repair and rebuild substandard homes in Vietnam for covered individuals and the families of covered individuals; and\n**(2)**\nmicro grants and loans to facilitate subsistence payments and poverty reduction for covered individuals and families of covered individuals.\n##### (d) For environmental remediation\n**(1) In general**\nThe Administrator of the United States Agency for International Development, or its successor, in coordination with the heads of other appropriate Federal agencies and nongovernmental organizations shall provide assistance to remediate those geographic areas of Vietnam that the Secretary determines contain high levels of Agent Orange.\n**(2) Priority**\nIn providing assistance under this subsection, the Administrator shall give priority to heavily sprayed areas, including areas that served as military bases where Agent Orange was handled, and areas where heavy spraying, spills, or air crashes resulted in harmful deposits of Agent Orange.\n##### (e) Administrative authorities\nThe Administrator shall\u2014\n**(1)**\nprovide assistance under this section (other than assistance under subsection (d)) through appropriate Vietnamese community and nongovernmental organizations and Vietnamese public agencies;\n**(2)**\nprovide assistance under this section to affected persons in all areas of Vietnam, including rural, mountainous, and urban areas; and\n**(3)**\nseek out and actively encourage other bilateral donors as well as United States and foreign business enterprises in Vietnam to support the goals of this section through development assistance and corporate philanthropy programs.\n##### (f) Covered individual defined\nIn this section, the term covered individual means an individual who\u2014\n**(1)**\nis a resident of Vietnam; and\n**(2)**\n**(A)**\nis affected by health issues related to exposure to Agent Orange which took place during the period beginning on January 1, 1961, and ending on May 7, 1975, or who lives or has lived in or near those geographic areas in Vietnam that continue to contain high levels of Agent Orange as described in subsection (d); or\n**(B)**\nis the child or descendant of an individual described in subparagraph (A), and is affected by health issues described in subparagraph (A).\n#### 4. Department of Health and Human Services health assessment and assistance for Vietnamese Americans\n##### (a) Health assessment\nThe Secretary of Health and Human Services shall make grants to appropriate public health organizations and Vietnamese American organizations for the purpose of conducting a broad health assessment of Vietnamese Americans who may have been exposed to Agent Orange and their children or descendants to determine the effects to their health of such exposure.\n##### (b) Assistance\nThe Secretary of Health and Human Services shall establish centers in locations in the United States where large populations of Vietnamese Americans reside for the purpose of providing assessment, counseling, and treatment for conditions related to exposure to Agent Orange. The Secretary may carry out this subsection through appropriate community and nongovernmental organizations or other suitable organizations, as determined by the Secretary.\n#### 5. Deadline for implementation\nNot later than 180 days after the date of enactment of this Act, the Administrator of the United States Agency for International Development, or its successor, and the Secretary of Health and Human Services shall each complete a plan for the implementation of the provisions of this Act, and the amendments made by this Act, that are applicable to such Secretary and shall issue a request for proposals, if applicable. The Administrator of the United States Agency for International Development, or its successor, and the Secretary of Health and Human Services shall each implement the applicable provisions of this Act by not later than 18 months after the date of enactment of this Act.\n#### 6. Quarterly reports\nNot later than 30 days after the last day of each fiscal quarter beginning on or after 18 months after the date of enactment of this Act, the Administrator of the United States Agency for International Development, or its successor, and the Secretary of Health and Human Services shall each submit to Congress a report on the implementation of the provisions of this Act applicable to such Secretary during the immediately preceding fiscal quarter.\n#### 7. Definition\nFor purposes of this Act, the term Agent Orange includes any chemical compound which became part, either by design or through impurities, of an herbicide agent used in support of the United States and allied military operations in the Republic of Vietnam.",
      "versionDate": "2025-04-28",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:55:44Z"
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
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3051ih.xml"
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
      "title": "Victims of Agent Orange Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Victims of Agent Orange Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the United States Agency for International Development, or its successor, and the Secretary of Health and Human Services to provide assistance for individuals affected by exposure to Agent Orange, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T06:18:32Z"
    }
  ]
}
```
