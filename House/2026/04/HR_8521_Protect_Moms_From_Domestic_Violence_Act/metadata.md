# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8521?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8521
- Title: Protect Moms From Domestic Violence Act
- Congress: 119
- Bill type: HR
- Bill number: 8521
- Origin chamber: House
- Introduced date: 2026-04-27
- Update date: 2026-05-06T19:52:27Z
- Update date including text: 2026-05-06T19:52:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-27: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-04-27: Introduced in House

## Actions

- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Introduced in House
- 2026-04-27 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-27",
    "latestAction": {
      "actionDate": "2026-04-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8521",
    "number": "8521",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Protect Moms From Domestic Violence Act",
    "type": "HR",
    "updateDate": "2026-05-06T19:52:27Z",
    "updateDateIncludingText": "2026-05-06T19:52:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-27",
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
      "actionDate": "2026-04-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-27",
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
          "date": "2026-04-27T16:02:00Z",
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
      "sponsorshipDate": "2026-04-27",
      "state": "PA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "MI"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "IL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8521ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8521\nIN THE HOUSE OF REPRESENTATIVES\nApril 27, 2026 Ms. Moore of Wisconsin (for herself, Mr. Fitzpatrick , Mrs. Dingell , Ms. Underwood , and Ms. Adams ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo study the extent to which individuals are more at risk of maternal morbidity or mortality as a result of being a victim of intimate partner violence.\n#### 1. Short title\nThis Act may be cited as the Protect Moms From Domestic Violence Act .\n#### 2. Study by National Academy of Medicine\n##### (a) In general\nThe Secretary of Health and Human Services shall seek to enter into an arrangement with the National Academy of Medicine (or, if the Academy declines to enter into such arrangement, another appropriate entity) to study how domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, intergenerational violence, trauma, or psychiatric disorders impact risk for maternal morbidity and maternal mortality, including intimate partner homicide.\n##### (b) Topics\nThe study under subsection (a) shall\u2014\n**(1)**\nexamine\u2014\n**(A)**\nwhether and how domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, intergenerational violence, trauma, or psychiatric disorders increase the risk of suicide, homicide, substance use, drug overdose, or poor birth outcomes among pregnant and postpartum persons; and\n**(B)**\nthe extent to which domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, intergenerational violence, trauma, or psychiatric disorders are social determinants of health; and\n**(2)**\ngive particular focus to impacts among diverse communities, including Black and African American, Hispanic and Latino, American Indian, Native Hawaiian, Pacific Islander, Alaskan Native, and LGBTQIA2S+ birthing persons, and adolescent mothers.\n#### 3. Grants for innovative approaches To improve maternal and child health outcomes\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, and in collaboration with the Assistant Secretary of the Administration for Children and Families, the Director of the Indian Health Service, the Assistant Secretary for Mental Health and Substance Use, and the Secretary of Veterans Affairs, shall award grants to eligible entities for developing and implementing innovative approaches, including culturally relevant public and provider education campaigns, to improve maternal and child health outcomes of victims of domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, intergenerational violence, trauma, or psychiatric disorders.\n##### (b) Report to Congress on best practices\nNot later than 3 years after the date of enactment of this Act, and every 3 years thereafter, the Secretary of Health and Services shall report to Congress on best practices for developing and implementing innovative approaches described in subsection (a).\n##### (c) Eligible entity\nTo seek a grant under this section, an entity shall be\u2014\n**(1)**\na State, local governmental entity, or federally recognized Tribal government;\n**(2)**\na nonprofit organization or community-based organization that provides prevention or intervention services related to domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, intergenerational violence, trauma, or psychiatric disorders;\n**(3)**\nan Indian Tribe, Tribal organization, or Urban Indian organization (as such terms are defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 ));\n**(4)**\na Tribal epidemiology center described in section 214 of the Indian Health Care Improvement Act ( 25 U.S.C. 1621m );\n**(5)**\na Federally qualified health center (as defined in section 1861(aa) of the Social Security Act ( 42 U.S.C. 1395x(aa) );\n**(6)**\na clinic certified as a certified community behavioral health clinic pursuant to section 223 of the Protecting Access to Medicare Act of 2014 ( 42 U.S.C. 1396a );\n**(7)**\nan entity, the principal purpose of which is to provide health care, such as a hospital, clinic, health department, or freestanding birth center;\n**(8)**\nan institution of higher education (as defined in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ));\n**(9)**\na substance use disorder treatment program with specialized services for parents; or\n**(10)**\na hospital or other health care facility of the Department of Veterans Affairs.\n##### (d) Priority in awarding grants\nIn awarding grants under this section, the Secretary of Health and Human Services shall give priority to applicants proposing\u2014\n**(1)**\nto address domestic violence, dating violence, sexual violence, and mental health and substance use disorders among pregnant persons;\n**(2)**\nto address issues relating to people experiencing domestic violence and sexual violence who are pregnant, persons at risk for becoming pregnant due to violence or abuse, and postpartum persons experiencing violence;\n**(3)**\nto develop or implement innovative approaches, including cultural bias training, antiracism training or implicit bias interruption or reduction strategies, and strategies to identify and prevent domestic violence within all racial, cultural, ethnic and community groups, including Black or African American, Hispanic or Latino, American Indian, Native Hawaiian, Pacific Islander, Alaskan Native, and LGBTQIA2S+ persons;\n**(4)**\nto develop or implement innovative approaches at Tribal epidemiology centers;\n**(5)**\nto develop or implement innovative approaches relating to the improvement of maternal health surveillance; or\n**(6)**\nto facilitate shared learning and dissemination of information through convening meetings with other grant recipients under this section.\n##### (e) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $15,000,000 for each of fiscal years 2027 through 2029.\n#### 4. Guidance\nNot later than 2 years after the date of enactment of this Act, the Secretary of Health and Human Services shall publish and disseminate to States, Indian Tribes, territories, health care providers, and managed care entities guidance on\u2014\n**(1)**\ndeveloping protocols on and providing\u2014\n**(A)**\nuniversal education on healthy relationships and intimate partner violence;\n**(B)**\nroutine assessment of intimate partner violence and mental and behavioral health conditions; and\n**(C)**\nhealth promotion and strategies for trauma-informed care plans; and\n**(2)**\ncreating sustainable partnerships between health care providers and community-based organizations that address domestic violence, dating violence, sexual assault, stalking, human trafficking, sex trafficking, child sexual abuse, forced marriage, reproductive coercion, or intergenerational violence.\n#### 5. Definitions\nIn this Act:\n**(1) Freestanding birth center**\nThe term freestanding birth center has the meaning given that term in section 1905(l) of the Social Security Act ( 42 U.S.C. 1396d(1) ).\n**(2) Maternal morbidity**\nThe term maternal morbidity means a health condition, including a mental health condition or substance use disorder, that\u2014\n**(A)**\nis attributed to or aggravated by pregnancy or childbirth; and\n**(B)**\nresults in significant short-term or long-term consequences to the health of the individual who was pregnant.\n**(3) Maternal mortality**\nThe term maternal mortality \u2014\n**(A)**\nmeans death that\u2014\n**(i)**\noccurs during, or within the 1-year period after, pregnancy; and\n**(ii)**\nis attributed to or aggravated by pregnancy-related or childbirth complications; and\n**(B)**\nincludes a suicide, drug overdose death, homicide (including a domestic violence-related homicide), or other death resulting from a mental health or substance use disorder attributed to or aggravated by pregnancy-related or childbirth complications.\n**(4) Postpartum**\nThe term postpartum means the 12-month period following childbirth.",
      "versionDate": "2026-04-27",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-04-27",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4387",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protect Moms From Domestic Violence Act",
      "type": "S"
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
        "updateDate": "2026-05-06T19:36:10Z"
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
      "date": "2026-04-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8521ih.xml"
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
      "title": "Protect Moms From Domestic Violence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Moms From Domestic Violence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To study the extent to which individuals are more at risk of maternal morbidity or mortality as a result of being a victim of intimate partner violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T08:18:27Z"
    }
  ]
}
```
