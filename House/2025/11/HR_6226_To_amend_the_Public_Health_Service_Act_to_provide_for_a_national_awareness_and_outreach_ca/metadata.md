# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6226?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6226
- Title: Latino Youth Mental Health Empowerment Act
- Congress: 119
- Bill type: HR
- Bill number: 6226
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-04T09:06:47Z
- Update date including text: 2026-02-04T09:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6226",
    "number": "6226",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Latino Youth Mental Health Empowerment Act",
    "type": "HR",
    "updateDate": "2026-02-04T09:06:47Z",
    "updateDateIncludingText": "2026-02-04T09:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:05:05Z",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NM"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IN"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6226ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6226\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Ms. Salinas (for herself, Ms. Stansbury , Ms. Vel\u00e1zquez , Mr. Carson , Mr. Thanedar , Mr. Torres of New York , Ms. Barrag\u00e1n , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for a national awareness and outreach campaign to improve mental health among the Hispanic and Latino youth population.\n#### 1. Short title\nThis Act may be cited as the Latino Youth Mental Health Empowerment Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nHispanic and Latino youth often experience and suffer from toxic stress, which stems from prolonged stress, trauma, or adverse childhood experiences.\n**(2)**\nAt least 78 percent of Hispanic and Latino youth suffer from at least one adverse childhood experience, which can harm a child\u2019s physical and mental health.\n**(3)**\nAmong Hispanic and Latino youth, approximately 60 percent were more likely to report poor mental health compared to their counterparts.\n**(4)**\nAbout 42 percent of Hispanic and Latino youth have reported persistent feelings of sadness or hopelessness.\n**(5)**\nApproximately 18 percent of Hispanic and Latino high school students have seriously contemplated suicide.\n**(6)**\nHispanic and Latinos are less likely than any other ethnic groups to receive clinical or school-based mental illness treatment and medication.\n**(7)**\nHispanic and Latino youth are less likely to use mental health care services compared to children of other ethnic groups.\n**(8)**\nThere are numerous factors that impact accessibility to mental health services and mental health outcomes. For instance, lower rates of health insurance, language and cultural barriers, and lack of parental education on mental health all contribute to adverse mental health outcomes for Hispanic and Latino youth.\n**(9)**\nIncreased awareness and outreach about mental health to Hispanic and Latino parents, caregivers, and youth are vital to ensure that Hispanic and Latino youth can experience positive mental health outcomes and reduced mental illness.\n#### 3. National hispanic and latino mental health awareness and outreach campaign\nPart D of title V of the Public Health Service Act ( 42 U.S.C. 290dd et seq. ) is amended by adding at the end the following new section:\n554. National hispanic and latino youth mental health awareness and outreach campaign (a) Study on prior campaigns Not later than 1 year after the date of the enactment of this section, the Secretary shall conduct a study on\u2014 (1) any education and outreach campaigns to promote mental health and reduce stigma associated with mental health that were carried out by the Secretary on or before the date of the enactment of the Latino Youth Mental Health Empowerment Act ; and (2) which messaging delivered through such campaigns was most effective within the Latino community. (b) Establishment of campaign (1) In general The Secretary, acting through the Assistant Secretary, shall develop and implement a national awareness and outreach campaign to promote mental health and reduce stigma associated with mental health within the Hispanic and Latino youth population. Such campaign shall be developed\u2014 (A) taking into account the results of the study conducted under subsection (a); (B) in coordination with the Director of the Office of Minority Health, the Director of the National Institutes of Health, the Director of the Centers for Disease Control and Prevention, and Assistant Secretary for Mental Health and Substance Use, and the Secretary of Education; and (C) in consultation with relevant advocacy and mental health organizations serving populations of Hispanic and Latino individuals or communities. (2) Elements of campaign The campaign under paragraph (1) shall\u2014 (A) develop a culturally- and linguistically-competent awareness campaign, targeted at Hispanic and Latino parents, caregivers, youth, teachers, school personnel, and school clinic staff to meet the diverse needs of Hispanic and Latino youth, including\u2014 (i) increasing awareness of symptoms associated with mental illnesses, including their prevalence and misconceptions among youth; (ii) increasing awareness of factors driving mental illness among Hispanic and Latino youth, including factors that are social determinants of health, taking into account differences within population subgroups, such as gender, gender identity, age, sexual orientation, ethnicity, geographic region or location, immigration status, and history of adverse childhood experiences; (iii) combatting the stigma of mental illnesses that are common in the Hispanic and Latino community, taking into account differences within such population subgroups; and (iv) increasing awareness of evidence-based, culturally-tailored, and trauma-informed mental illness screening, intervention, and treatment options, taking into account differences within such population subgroups; and (B) develop a culturally and linguistically competent outreach campaign, targeted at Hispanic and Latino parents, caregivers, youth, teachers, school personnel, and school clinic staff to meet the diverse needs of Hispanic and Latino youth, including\u2014 (i) creating and distributing mental health materials and resources (including materials relating to the National Suicide Prevention and Mental Health Hotline under section 520E\u20133) in collaboration with local, State, and national community advocates and stakeholders, taking into account differences within population subgroups, such as gender, gender identity, age, sexual orientation, ethnicity, and geographic region or location; (ii) hosting in-person and virtual mental health workshops at relevant locations, including elementary schools and secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965), community centers, and other appropriate sites; (iii) providing youth mental health first aid training to parents, caregivers, teachers, school personnel, and school clinic staff, and other personnel that consistently interact or work with the target population; (iv) establishing partnerships between local, State, and national mental health agencies and elementary schools and secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965), after-school programs, and other appropriate sites that serve Hispanic and Latino youth; and (v) providing mental health screenings and on-site consultations at elementary schools and secondary schools (as such terms are defined in section 8101 of the Elementary and Secondary Education Act of 1965), community centers, and other appropriates sites. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section $5,000,000 for each of fiscal years 2026 through 2030. .\n#### 4. Study and report on the Hispanic and Latino youth mental health crisis\n##### (a) Study\n**(1) In general**\nThe Secretary, acting through the Assistant Secretary for Mental Health and Substance Use, in coordination with the Director of the National Institutes of Health, the Director of the Centers for Disease Control and Prevention, the Director of the Office of Minority Health, and the Surgeon General of the Public Health Service, shall conduct a study on mental health among Hispanic and Latino youth.\n**(2) Elements**\nSuch study required under paragraph (1) shall include an assessment of\u2014\n**(A)**\nthe prevalence and risk factors of mental health and substance use disorders among Hispanic and Latino youth;\n**(B)**\nthe prevalence of attempted suicide and death by suicide among Hispanic and Latino youth;\n**(C)**\nthe prevalence of treatment for mental health and substance use disorders among Hispanic and Latino youth;\n**(D)**\nthe awareness and utilization of the 9\u20138\u20138 National Suicide Prevention and Mental Health Hotline under section 520E\u20133 of the Public Health Service Act ( 42 U.S.C. 290bb\u201336c ) and other mental health and suicide prevention hotlines among Hispanic and Latino youth;\n**(E)**\nthe awareness, utilization, and availability of mobile crisis care teams, dispatched through the 9\u20138\u20138 National Suicide Prevention and Mental Health Hotline or other mental health and suicide prevent hotlines, among Hispanic and Latino youth; and\n**(F)**\nthe awareness, utilization, and availability of crisis centers for Hispanic and Latino youth in acute mental health or substance use crisis.\n##### (b) Report\nNot later than 1 year after the date of the enactment of the Latino Youth Mental Health Empowerment Act , the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a report on the findings of the study conducted under subsection (a), including\u2014\n**(1)**\nidentification of the barriers to accessing mental health services and treatment for Hispanic and Latino youth;\n**(2)**\nrecommendations to improve mental health services, outreach, and treatment among Hispanic and Latino youth;\n**(3)**\nrecommendations to reduce rates of mental health and substance use disorders and suicide among Hispanic and Latino youth;\n**(4)**\nrecommendations to improve awareness and utilization of the 9\u20138\u20138 National Suicide Prevention and Mental Health Hotline and other mental health and suicide prevention hotlines among Hispanic and Latino youth;\n**(5)**\nrecommendations to improve access to, and utilization of, mobile crisis care teams among Hispanic and Latino youth, when clinically appropriate;\n**(6)**\nrecommendation to improve access to, and utilization of, crisis centers for Hispanic and Latino youth in acute mental health or substance use crisis, when clinically appropriate; and\n**(7)**\nsuch other recommendations as the Secretary determines appropriate.\n##### (c) Data\nAny data included in the study or report under this section shall be disaggregated by race, ethnicity, age, sex, gender identity, sexual orientation, geographic region, disability status, and other relevant factors, in a manner that, as appropriate and feasible, protects personal privacy and that is consistent with applicable Federal and State privacy law.\n##### (d) Authorization of appropriations\nFor purposes of carrying out this section, there is authorized to be appropriated $1,000,000 for fiscal year 2026.\n#### 5. Study and report on the Hispanic and Latino mental health workforce shortage\n##### (a) Study\n**(1) In general**\nThe Secretary, acting through the Assistant Secretary for Mental Health and Substance Use, in coordination with the Administrator of the Health Resources and Services Administration, the Director of the Office of Minority Health, the Surgeon General of the Public Health Service, and the Secretary of Labor, and shall conduct a study on strategies for increasing the mental health professional workforce that identify as Hispanic or Latino.\n**(2) Elements**\nSuch study required under paragraph (1) shall address\u2014\n**(A)**\nthe total number of licensed clinical and non-clinical mental health providers who identify as Hispanic or Latino;\n**(B)**\nwith respect to each such provider, information regarding the current license type, geographic location of practice, and type of employer (such as a hospital, federally-qualified health center (as defined in section 1861(aa)(4) of the Social Security Act ( 42 U.S.C. 1395x(aa)(4) ))), elementary school or secondary school (as such terms are defined in section 8101 of the of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ), or private practice);\n**(C)**\ninformation regarding the languages spoken among providers, including the level of proficiency in speaking, reading, and writing such languages; and\n**(D)**\nthe current enrollment of Hispanic and Latino individuals in mental health professional education programs.\n##### (b) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions of the Senate and the Committee on Energy and Commerce of the House of Representatives, and make publicly available, a report on the findings of the study conducted under subsection (a). Such report shall\u2014\n**(1)**\nassess Hispanic and Latino clinical and non-clinical mental health providers\u2019 knowledge and awareness of the barriers to quality mental health care services faced by Hispanic and Latino individuals;\n**(2)**\ninclude recommendations for actions to be taken by the Secretary to increase the number of Hispanic and Latino clinical and non-clinical mental health professionals;\n**(3)**\ninclude recommendations to improve enrollment in mental health professional education programs among Hispanic and Latino individuals; and\n**(4)**\ninclude such other recommendations as the Secretary determines appropriate.\n##### (c) Data\nAny data included in the study or report under this section shall be disaggregated by race, ethnicity, age, sex, gender identity, sexual orientation, geographic region, disability status, and other relevant factors, in a manner that protects personal privacy and that is consistent with applicable Federal and State privacy law.\n##### (d) Definition\nIn this section, the term clinical and non-clinical mental health provider means any individual licensed to provide mental health or substance use disorder services, including in the professions of social work, psychology, psychiatry, marriage and family therapy, mental health counseling, substance use disorder counseling, peer support, primary care, pediatrics, nursing, and other fields as determined by the Secretary.\n##### (e) Authorization of appropriations\nFor purposes of carrying out this section, there is authorized to be appropriated $1,000,000 for fiscal year 2026.",
      "versionDate": "2025-11-20",
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
        "updateDate": "2025-12-12T16:13:53Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6226ih.xml"
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
      "title": "Latino Youth Mental Health Empowerment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Latino Youth Mental Health Empowerment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for a national awareness and outreach campaign to improve mental health among the Hispanic and Latino youth population.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:18:26Z"
    }
  ]
}
```
