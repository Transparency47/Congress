# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4841
- Title: Stomach Cancer Prevention and Early Detection Act
- Congress: 119
- Bill type: HR
- Bill number: 4841
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-01-28T09:05:19Z
- Update date including text: 2026-01-28T09:05:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-01 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4841",
    "number": "4841",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001080",
        "district": "28",
        "firstName": "Judy",
        "fullName": "Rep. Chu, Judy [D-CA-28]",
        "lastName": "Chu",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Stomach Cancer Prevention and Early Detection Act",
    "type": "HR",
    "updateDate": "2026-01-28T09:05:19Z",
    "updateDateIncludingText": "2026-01-28T09:05:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Armed Services, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:09:20Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-01T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-01T14:00:45Z",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "SC"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "WI"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4841ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4841\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Ms. Chu (for herself and Mr. Wilson of South Carolina ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committees on Armed Services , and Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Director of the National Cancer Institute to conduct a review of the current state of stomach cancer incidence, prevention, screening, awareness, and future public health importance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stomach Cancer Prevention and Early Detection Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nStomach cancer accounts for about 1.5 percent of all new cancers diagnosed in the United States each year.\n**(2)**\nIt is estimated that there will be nearly 30,300 new cases of stomach cancer in 2025.\n**(3)**\nThere are disparities in stomach cancer incidence and mortality among racial and ethnic groups in the United States.\n**(4)**\nWhile there has been a decline in stomach cancer incidence, the lack of awareness and focus on risk factors and early detection through screening and surveillance may cause individuals at high risk for the disease to dismiss their symptoms.\n**(5)**\nEstablishing a basis for stomach cancer prevalence, awareness, current screening, and implications for future public health importance will allow for\u2014\n**(A)**\nmore effective outreach and screening among individuals at risk;\n**(B)**\nincreased awareness and education among the general public to prevent stomach cancer; and\n**(C)**\nincreased awareness and education among health care providers regarding gastric cancer disparities, screening, treatment, and monitoring.\n#### 3. NCI review on current state of stomach cancer incidence, prevention, screening, awareness, and future public health importance\n##### (a) Review\nThe Director of the National Cancer Institute shall conduct a review of\u2014\n**(1)**\nthe current incidence of stomach cancer in the United States;\n**(2)**\nthe risk factors for stomach cancer, including the incidence of such risk factors among high-risk populations and the general public;\n**(3)**\nthe optimal age range to test for and treat Helicobacter pylori (H. pylori) infection, as a risk factor, for the purpose of primary prevention in high-risk populations and the general population;\n**(4)**\nthe availability and frequency of screening for stomach cancer, including utilization and effectiveness, among high-risk populations;\n**(5)**\nthe availability and effectiveness of endoscopic screenings in high-risk populations;\n**(6)**\nthe availability and effectiveness of endoscopic resection and surveillance endoscopy for patients with confirmed gastric intestinal metaplasia (GIM) with high-grade dysplasia and early gastric cancer;\n**(7)**\nthe benefits of surveillance endoscopy for patients at elevated risk, including patients with gastric intestinal metaplasia (GIM) who are at increased risk of gastric cancer due to ethnic background, family history, or other risk stratification parameters such as smoking and H. pylori infection;\n**(8)**\ncurrent awareness and education about stomach cancer risk factors, prevention, symptoms, screening, and treatment options among high-risk populations and the general public; and\n**(9)**\ncurrent Federal efforts to increase awareness and education of stomach cancer among high-risk populations and the general public.\n##### (b) Report\nNot later than 18 months after the date of enactment of this Act, the Director of the National Cancer Institute shall\u2014\n**(1)**\nsubmit to the Congress a report on the results of the review under subsection (a); and\n**(2)**\ninclude in such report recommendations for\u2014\n**(A)**\nestablishing a clear definition of high-risk populations in the United States;\n**(B)**\ninforming researchers, clinicians, physicians, patients, and other relevant stakeholders on\u2014\n**(i)**\nidentifying high-risk individuals; and\n**(ii)**\neffective methods for detecting precancerous lesions and early gastric cancer;\n**(C)**\nestablishing routine screening guidelines for stomach cancer; and\n**(D)**\nactions to improve research on, prevention and early diagnosis of, and screening and treatment for stomach cancer.\n#### 4. Department of Defense study on stomach cancer incidence and risk factors among military personnel\n##### (a) Study\nThe Secretary of Defense, in coordination with the Director of the National Cancer Institute and the Director of the Centers for Disease Control and Prevention, shall conduct a study on the incidence, risk factors, prevention, and early detection of stomach cancer among members of the Armed Forces and former members of the Armed Forces.\n##### (b) Elements\nThe study under subsection (a) shall include\u2014\n**(1)**\nan examination of\u2014\n**(A)**\nthe incidence, prevalence, and mortality rates of stomach cancer among members of the Armed Forces serving on active duty and former members of the Armed Forces who served on active duty;\n**(B)**\nthe identification of service-related or deployment-related risk factors, including exposure to burn pits, hazardous chemicals, contaminated water, occupational hazards, and endemic infections such as Helicobacter pylori (H. pylori);\n**(C)**\ndisparities in stomach cancer outcomes based on race, ethnicity, gender, Armed Force, or geographic deployment history within military populations;\n**(D)**\nthe availability and use of stomach cancer screening, diagnostic, and treatment services within the military health system and the health system of the Department of Veterans Affairs; and\n**(E)**\nopportunities to improve prevention and early detection strategies within the military health system and the health system of the Department of Veterans Affairs; and\n**(2)**\nrelevant coordination with the Surveillance, Epidemiology, and End Results Program and other national cancer registries to ensure comprehensive data collection and analysis.\n##### (c) Report\nNot later than 18 months after the date of the enactment of this Act, the Secretary of Defense shall submit to Congress a report on the findings of the study under subsection (a), including\u2014\n**(1)**\npolicy and programmatic recommendations to reduce stomach cancer incidence and mortality among members of the Armed Forces and former members of the Armed Forces; and\n**(2)**\nproposed strategies for integrating stomach cancer awareness, screening, and treatment protocols into the military health system and the health system of the Department of Veterans Affairs.",
      "versionDate": "2025-08-01",
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
        "updateDate": "2025-09-18T15:15:51Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4841ih.xml"
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
      "title": "Stomach Cancer Prevention and Early Detection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stomach Cancer Prevention and Early Detection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Director of the National Cancer Institute to conduct a review of the current state of stomach cancer incidence, prevention, screening, awareness, and future public health importance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:21Z"
    }
  ]
}
```
