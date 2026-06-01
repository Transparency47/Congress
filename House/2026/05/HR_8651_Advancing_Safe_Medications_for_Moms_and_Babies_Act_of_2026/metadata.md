# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8651
- Title: Advancing Safe Medications for Moms and Babies Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8651
- Origin chamber: House
- Introduced date: 2026-05-04
- Update date: 2026-05-18T16:13:07Z
- Update date including text: 2026-05-18T16:13:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-04: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-05-04: Introduced in House

## Actions

- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Introduced in House
- 2026-05-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-04",
    "latestAction": {
      "actionDate": "2026-05-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8651",
    "number": "8651",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001066",
        "district": "14",
        "firstName": "Kathy",
        "fullName": "Rep. Castor, Kathy [D-FL-14]",
        "lastName": "Castor",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Advancing Safe Medications for Moms and Babies Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-18T16:13:07Z",
    "updateDateIncludingText": "2026-05-18T16:13:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-04",
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
      "actionDate": "2026-05-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-04",
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
          "date": "2026-05-04T14:31:25Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "PA"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8651ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8651\nIN THE HOUSE OF REPRESENTATIVES\nMay 4, 2026 Ms. Castor of Florida (for herself, Mr. Fitzpatrick , and Ms. Underwood ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo implement certain recommendations to promote the inclusion of pregnant and lactating women in clinical research, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Safe Medications for Moms and Babies Act of 2026 .\n#### 2. Updating FDA regulations to include pregnant women in clinical trials\n##### (a) Purposes\nThe purposes of this section are\u2014\n**(1)**\nto facilitate compliance with applicable Federal regulations relating to the protection of pregnant women participating in research as subjects; and\n**(2)**\nto promote the inclusion of pregnant women in clinical research.\n##### (b) Harmonization\nFor the purposes specified in subsection (a), the Secretary of Health and Human Services (referred to in this Act as the Secretary ), acting through the Commissioner of Food and Drugs, shall, to the extent practicable and consistent with other applicable Federal statutory law, issue such regulations as may be appropriate to harmonize the regulations of the Food and Drug Administration relating to the protection of human subjects, including parts 50 and 56 of title 21, Code of Federal Regulations, with the regulations of the Department of Health and Human Services relating to the inclusion of pregnant women as subjects in clinical research.\n##### (c) Deadline\nThe Secretary of Health and Human Services shall finalize the regulations required by subsection (b) not later than 180 days after the date of enactment of this Act.\n#### 3. Raising awareness of research that includes pregnant and lactating women\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary) , in consultation with the heads of other relevant Federal agencies, including the Director of the Centers for Disease Control and Prevention and the Director of the National Institutes of Health, shall establish and implement an education campaign designed to educate patients, their families, health care providers, and other target audiences on\u2014\n**(1)**\nhow including pregnant and lactating women in clinical research can benefit maternal and infant health;\n**(2)**\navailable registries and clinical trials that include pregnant and lactating women;\n**(3)**\nthe role registries and other postmarket surveillance activities have in studying drugs used by pregnant and lactating women; and\n**(4)**\nhow pregnant and lactating women can easily identify and enroll in clinical trials or registries.\n##### (b) Consultation\nIn carrying out this section, the Secretary shall consult with\u2014\n**(1)**\norganizations with expertise related to the health of women and infants, including such organizations representing populations with high rates of maternal mortality and morbidity;\n**(2)**\nrepresentatives from relevant medical societies with subject matter expertise on pregnant women, lactating women, or infants;\n**(3)**\nrelevant industry representatives; and\n**(4)**\nother representatives, as appropriate.\n##### (c) Planning\nIn establishing the campaign under subsection (a), the Secretary, in consultation with the heads of other relevant Federal agencies, shall\u2014\n**(1)**\nconduct a needs assessment to\u2014\n**(A)**\nevaluate existing resources; and\n**(B)**\nidentify barriers to awareness and opportunities to fill gaps and address barriers;\n**(2)**\nidentify target audiences for the campaign;\n**(3)**\nidentify resource needs for each target audience and best practices to reach each such audience; and\n**(4)**\ntest appropriate messaging strategies, including risk communication messaging, for each target audience.\n##### (d) Dissemination\nThe Secretary shall publish on a public website, and regularly update, the campaign materials described in this section, and shall ensure that such website\u2014\n**(1)**\nincludes information on clinical trials and registries enrolling pregnant and lactating women; and\n**(2)**\nprovides a user-friendly interface for patients, their families, health care providers, and other target audiences.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2027 through 2031.\n#### 4. Research prioritization process for pregnant and lactating women at the Eunice Kennedy Shriver National Institute of Child Health and Human Development\n##### (a) In general\nThe Director of the National Institutes of Health, acting through the Director of the Eunice Kennedy Shriver National Institute of Child Health and Human Development (referred to in this section as NICHD ), shall carry out priority research projects on existing and new drugs prescribed for pregnant and lactating women.\n##### (b) Research prioritization process\nThe Director of the National Institutes of Health shall establish a research prioritization process to determine which proposed research projects should receive priority funding under this section. Such research prioritization process shall take into account the following factors:\n**(1)**\nThe available evidence, including whether there is an unmet medical need or gap in scientific information relevant to treatment of pregnant and lactating women with specific diseases or conditions.\n**(2)**\nThe feasibility of research, including the prevalence of a disease or condition in pregnant and lactating women and the availability of investigators with expertise in studying such disease or condition.\n**(3)**\nThe potential impact of research, including the severity of the disease or condition in pregnant and lactating women, the current cost of treating the disease or condition in pregnant and lactating women, the frequency of use of the drug in pregnant and lactating women, and the availability of alternative treatments for the disease or condition in pregnant and lactating women.\n##### (c) Consultation\nIn developing the research prioritization process described in subsection (b), the Director of the National Institutes of Health shall seek feedback from\u2014\n**(1)**\nthe existing research networks of the NICHD with expertise in clinical research involving pregnant and lactating women;\n**(2)**\nrelevant medical societies with subject matter expertise on pregnant women, lactating women, or children; and\n**(3)**\norganizations with expertise related to the health of pregnant women, lactating women, or children, including such organizations representing populations with high rates of maternal mortality and morbidity.\n##### (d) Research requirements\nThe Director of the National Institutes of Health shall ensure that\u2014\n**(1)**\nresearch projects carried out under subsection (a) are conducted by individuals who have the expertise to rigorously evaluate the best-available scientific research; and\n**(2)**\nthe findings from such research projects are based on a preponderance of the best-available, peer-reviewed scientific evidence.\n##### (e) Public comment\nThe Secretary shall provide an opportunity for public comment on the program under this section.\n##### (f) Accountability and oversight\n**(1) Work plan**\nNot later than 180 days after the date of enactment of this Act, the Director of the National Institutes of Health shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Appropriations of the Senate and the Committee on Energy and Commerce and the Committee on Appropriations of the House of Representatives a work plan for\u2014\n**(A)**\nfunding priority research projects under subsection (a); and\n**(B)**\ndeveloping the research prioritization process under subsection (b).\n**(2) Reports**\nNot later than October 1 of each fiscal year for the 5 fiscal years beginning immediately after the date of enactment of this Act, the Director of the National Institutes of Health shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Appropriations of the Senate and the Committee on Energy and Commerce and the Committee on Appropriations of the House of Representatives a report on the program under this section, including\u2014\n**(A)**\nthe amount of money obligated or expended in the prior fiscal year for each priority research project under subsection (a);\n**(B)**\na description of each such project; and\n**(C)**\nthe rationale for prioritizing each such project according to the process under subsection (b).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section such sums as may be necessary for each of fiscal years 2027 through 2031.",
      "versionDate": "2026-05-04",
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
        "updateDate": "2026-05-18T16:13:06Z"
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
      "date": "2026-05-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8651ih.xml"
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
      "title": "Advancing Safe Medications for Moms and Babies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-05T08:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Safe Medications for Moms and Babies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-05T08:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To implement certain recommendations to promote the inclusion of pregnant and lactating women in clinical research, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-05T08:18:38Z"
    }
  ]
}
```
