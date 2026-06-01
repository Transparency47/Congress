# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5162?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5162
- Title: Colorectal Cancer Early Detection Act
- Congress: 119
- Bill type: HR
- Bill number: 5162
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-01-09T09:06:47Z
- Update date including text: 2026-01-09T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5162",
    "number": "5162",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Colorectal Cancer Early Detection Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:06:47Z",
    "updateDateIncludingText": "2026-01-09T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:00:25Z",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "TN"
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
      "sponsorshipDate": "2026-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5162ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5162\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Ms. Stevens (for herself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to make grants to States to increase awareness and education for colorectal cancer and improve early detection of colorectal cancer in young individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Colorectal Cancer Early Detection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn the United States, colorectal cancer is the third leading cause of cancer-related deaths in men and the fourth leading cause in women. Colorectal cancer is the second most common cause of cancer deaths when numbers for men and women are combined.\n**(2)**\nIn the United States, there were over 141,000 new colorectal cancer cases and 52,000 new colorectal cancer deaths reported in 2021. It is estimated that there will be over 154,270 new cases of colorectal cancer and 52,900 cases of colorectal cancer deaths in 2025.\n**(3)**\nColorectal cancer rates have been increasing in young patients. About 1 in 5 cases of colorectal cancer were in individuals age 54 and younger.\n**(4)**\nIn early 2023, it was reported that about 20 percent of diagnoses of colorectal cancer were among patients under the age of 55. Additionally, half of all early-onset colorectal cancer cases are diagnosed in individuals under 45 years old.\n**(5)**\nColorectal cancer cases among individuals ages 20 to 39 are expected to increase by 90 percent by 2030. Additionally, colorectal cancer is projected to be the leading cause of cancer-related deaths for individuals under 50 years of age by 2030.\n#### 3. CDC State grants for colorectal cancer awareness, education, and early detection among young individuals\n##### (a) Definitions\nIn this section:\n**(1) State**\nThe term State means each of the several States, the District of Columbia, and any territory or possession of the United States.\n**(2) Young individual**\nThe term young individual means an individual who has not attained the age of 45.\n##### (b) In general\nThe Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, (in this section referred to as the Secretary ) may make grants to States, on a competitive basis, for the purpose of increasing awareness and education for colorectal cancer and early detection of colorectal cancer in young individuals.\n##### (c) Application\nTo be eligible for a grant under this section, a State shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including a detailed description of the State\u2019s plan to implement the grant. Such description shall include how the State will use the grant to\u2014\n**(1)**\nconduct outreach and education regarding incidence of colorectal cancer and risk factors, with an emphasis on\u2014\n**(A)**\nyoung individuals with an increased risk or high risk for colorectal cancer, including\u2014\n**(i)**\nyoung individuals with a family history of colorectal cancer or advanced adenomatous polyps;\n**(ii)**\nyoung individuals with a personal history of inflammatory bowel disease (commonly known as IBD ), including ulcerative colitis and Crohn\u2019s disease of the colon;\n**(iii)**\nyoung individuals with an inherited syndrome, including Lynch syndrome, familial adenomatous polyposis, and other inherited syndromes linked to colorectal cancer;\n**(iv)**\nyoung individuals with signs and symptoms of colorectal cancer, particularly rectal bleeding and iron deficiency anemia; and\n**(v)**\nother young individuals with risk factors (such as risk factors identified by nationally recognized guidelines) that put such individuals at increased risk for colorectal cancer, as determined by the Secretary; and\n**(B)**\nindividuals in underserved and rural areas, individuals who identify as American Indian, Alaska Native, or African American, and individuals with type 2 diabetes, for the purposes of\u2014\n**(i)**\nidentifying individuals who are at increased risk or high risk for colorectal cancer (including young individuals described in clauses (i) through (v) of subparagraph (A)) and would benefit from early detection before age 45; and\n**(ii)**\nproviding education to initiate early detection at age 45 for individuals who are not at increased risk or high risk for colorectal cancer;\n**(2)**\npartner with hospitals, clinics, Tribal organizations (as defined in section 4 of the Indian Self-Determination and Education Assistance Act), nonprofit organizations, institutions of higher education, colorectal cancer prevention and control programs, and other relevant entities and programs to enhance outreach, education, and early detection efforts with respect to colorectal cancer in young individuals; and\n**(3)**\nconduct activities to increase awareness and education for colorectal cancer and improve early detection of colorectal cancer in young individuals, including navigation and program evaluation.\n##### (d) Use of funds\nA grant under this section may be used for any of the following:\n**(1)**\nTo support early detection and diagnostic testing for colorectal cancer in young individuals deemed to be at increased risk or high risk of colorectal cancer as part of a preventive health measure strategy.\n**(2)**\nTo provide appropriate referrals for medical treatment, including genetic testing and counseling of such young individuals, and to ensure, to the extent practicable, the provision of appropriate follow-up and surveillance services.\n**(3)**\nTo develop and implement a public awareness and education campaign for the early detection, signs and symptoms, risk factors, and control management of colorectal cancer, specifically in young individuals.\n**(4)**\nTo conduct education and outreach to health professionals (including allied health professionals) on conducting and interpreting colorectal cancer screening and diagnostic tests and the latest advancements in the early detection of colorectal cancer, with a focus on symptoms, genetic risk factors, family history, and care for young individuals.\n**(5)**\nTo establish mechanisms through which the States can monitor the quality of screening and diagnostic procedures for colorectal cancer among young individuals, including the interpretation of such procedures.\n**(6)**\nTo conduct surveillance to help determine other risk factors for colorectal cancer.\n**(7)**\nTo develop strategies to capture and assess family history and genetic predispositions to colorectal cancer in young individuals.\n**(8)**\nTo establish patient navigation support to assist individuals through the process of screening, particularly those at increased risk or high risk for colorectal cancer.\n**(9)**\nTo design clinician decision support tools based on clinical practice guidelines for early detection of colorectal cancer in young individuals.\n**(10)**\nTo monitor and evaluate activities conducted under paragraphs (1) through (9) to determine the effectiveness of such activities to inform continuous improvement of such activities.\n##### (e) Grant period\nA grant under this section shall be for a period of 5 years, and may be renewed at the discretion of the Secretary.\n##### (f) Return of unspent grant funds\nEach State that receives a grant under this section shall return, not later than 6 months after the date on which the period of such grant ends, any grant funds that were not expended by such State during the grant period.\n##### (g) Report\nNot later than 5 years after receiving a grant under this section (including a renewal of a grant), a State shall submit to the Secretary a report describing how the State used such grant.",
      "versionDate": "2025-09-04",
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
        "name": "Health",
        "updateDate": "2025-09-23T17:26:23Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5162ih.xml"
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
      "title": "Colorectal Cancer Early Detection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Colorectal Cancer Early Detection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, to make grants to States to increase awareness and education for colorectal cancer and improve early detection of colorectal cancer in young individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T08:18:25Z"
    }
  ]
}
```
