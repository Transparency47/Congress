# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4744?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4744
- Title: Community Mental Wellness and Resilience Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4744
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-05-14T08:08:01Z
- Update date including text: 2026-05-14T08:08:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4744",
    "number": "4744",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Community Mental Wellness and Resilience Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-14T08:08:01Z",
    "updateDateIncludingText": "2026-05-14T08:08:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:00:15Z",
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
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NE"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "FL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "VT"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "DE"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NM"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4744ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4744\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. Tonko (for himself, Mr. Fitzpatrick , Mr. Bacon , and Ms. Castor of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services to promote mental wellness and resilience and prevent and heal mental health, behavioral health, and psychosocial conditions through developmentally and culturally appropriate community programs, and award grants for the purpose of establishing, operating, or expanding community-based mental wellness and resilience programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Mental Wellness and Resilience Act of 2025 .\n#### 2. Grant program for community mental wellness and resilience programs\nTitle III of the Public Health Service Act is amended by inserting after section 317V ( 42 U.S.C. 247b\u201324 ) the following:\n317W. Grant program for community mental wellness and resilience programs (a) Grants (1) Planning grants (A) Awards The Secretary shall award grants to eligible organizations\u2014 (i) to organize a mental wellness and resilience coordinating network; (ii) to perform assessments of need with respect to community mental wellness and resilience; and (iii) to prepare an application for a grant under paragraph (2). (B) Amount The amount of a grant under subparagraph (A), with respect to any eligible organization seeking such a grant shall not exceed $250,000. (C) Eligible organization defined In this paragraph, the term eligible organization means an organization that\u2014 (i) is a nonprofit or community-based entity eligible to be a part of the resilience coordinating network (as defined in subsection (c)); and (ii) has documented support from at least 3 other such entities. (2) Program grants (A) Awards The Secretary shall carry out a program of awarding grants to mental wellness and resilience coordinating networks, on a competitive basis, for the purpose of establishing, operating, or expanding community mental wellness and resilience programs. (B) Amount The amount of a grant under subparagraph (A) shall not exceed $500,000 each year over a period not to exceed four years. (C) Rural set aside (i) In general Of the funds appropriated to carry out this section for a fiscal year, 20 percent of such funds shall be reserved to award grants to community mental wellness and resilience programs in rural areas. (ii) Rural area described For purposes of clause (i), a rural area is a region outside of an urban or suburban area. (iii) Inclusion For purposes of clause (ii), a rural area may include individuals and organizations from multiple towns in the county or region involved. (b) Program requirements A program carried out using funds awarded under subsection (a)(2) shall take a public health approach to mental health prevention and promotion, using the best available evidence, to strengthen the entire community\u2019s psychological and emotional wellness and resilience, including by\u2014 (1) collecting and analyzing information from residents of the community as well as quantitative data to identify\u2014 (A) protective factors that enhance and sustain the community\u2019s capacity for mental wellness and resilience; and (B) risk factors that undermine such capacity; (2) strengthening such protective factors and addressing such risk factors; (3) building awareness, skills, tools, and leadership in the community to\u2014 (A) facilitate using a public health approach to mental health; and (B) detect, prevent, and heal mental health, behavioral health, and psychosocial conditions among all adults and youth; and (4) developing, implementing, and continually evaluating and improving a comprehensive strategic plan for carrying out the activities described in paragraphs (1), (2) and (3) that includes utilizing developmentally, linguistically, and culturally appropriate evidence-based, evidence-informed, promising-best, or indigenous practices for\u2014 (A) engaging residents in building social connections, including across cultural, geographic, and economic boundaries; (B) enhancing local economic, social, and environmental conditions, including with respect to the built environment; (C) becoming trauma-informed and learning simple self-administrable mental wellness and resilience skills; (D) engaging in community activities that strengthen mental wellness and resilience; (E) partaking in nonclinical group and community-minded prevention and recovery programs; and (F) other activities to promote mental wellness and resilience and prevent or heal individual and community traumas. (c) Resilience coordinating network (1) In general In this section, the term resilience coordinating network means a network that is composed of 1 or more representatives from at least 5 of the categories listed in paragraph (2). (2) Categories The categories listed in this paragraph are the following: (A) Grassroots groups, community-based organizations, neighborhood associations, and volunteer civic organizations. (B) Elementary and secondary schools, high-needs schools, institutions of higher education, including community colleges, job-training programs, and other education or training agencies or organizations. (C) Youth serving organizations, such as youth after-school and summer programs. (D) Parental, family, and early childhood education programs. (E) Faith and spirituality organizations. (F) Senior care organizations. (G) Climate change mitigation and adaptation, and environmental conservation, groups and organizations. (H) Social and environmental justice groups and organizations. (I) Disaster preparedness and emergency response groups and organizations. (J) Businesses and business associations. (K) Police, fire, and other agencies and organizations involved with community safety, security, and the justice system. (L) Social work, mental health, behavioral health, substance use, physical health, public health, and other professionals, groups, organizations, agencies, and institutions in the human health and social services fields. (M) The general public, including individuals who have experienced adverse mental health or behavioral health conditions who can represent and engage with populations and sectors relevant to the community. (d) Technical assistance The Secretary shall provide, directly or through grants to, or contracts with public or private entities, to eligible organizations and resilience coordinating networks technical assistance\u2014 (1) in developing applications for grants under paragraph (1) or (2) of subsection (a); and (2) by sharing best practices learned from resilience coordinating networks. (e) Report (1) Submission Not later than December 31, 2030, the Secretary shall submit a report to the Congress on the results of the grants under subsection (a)(1). (2) Contents Such report shall include a summary of the best practices used by grantees in establishing, operating, or expanding community mental wellness and resilience programs, and the outputs and outcomes achieved. (f) Definitions In this section: (1) The term public health approach to mental health refers to methods that\u2014 (A) take a population-level approach to promote mental wellness and resilience to prevent problems before they emerge, intervene before they become more severe, and heal them when they do appear, not merely treating individuals one at a time after symptoms of pathology appear; and (B) address mental health and psychosocial problems by\u2014 (i) identifying and strengthening existing protective factors, and forming new ones, that buffer people from and enhance their capacity for psychological, emotional, and behavioral wellness and resilience for adversities; (ii) taking a holistic systems perspective that recognizes that most mental health, behavioral health, and psychosocial conditions result from numerous interrelated personal, family, social, economic, and environmental factors that require multipronged community-based interventions; and (iii) using the best available evidence to take action and implement strategies that support mental health prevention and recovery efforts. (2) The term community means people, groups, and organizations that reside in or work within a specific geographic area, such as a city, neighborhood, subdivision, or urban, suburban, or rural locale. (3) The term community trauma means a traumatic event or events that are shared by a community and that have lasting adverse effects on the health and well-being of the community. (4) The term protective factors means strengths, skills, resources, and characteristics that\u2014 (A) are associated with a lower likelihood of negative outcomes of adversities; or (B) reduce the impact on people of toxic stresses or a traumatic experience. (5) The term mental wellness means a state of well-being in which an individual experiences positive emotional functioning, pursues self-defined goals, establishes and maintains meaningful relationships, and feels a sense of meaning and purpose. At the individual level, well-being is based on fundamental family, social, cognitive, and emotional skills and supports that help individuals react, cope, and adapt in healthy ways to stress, uncertainty, adversity, trauma, and change. At the community level, well-being is influenced by the social, economic, educational, and environmental factors and conditions that either enhance or diminish well-being within the community. (6) The term psychosocial problem refers to social and environmental structures and processes that adversely effect and influence an individual\u2019s mental state or community health. (7) The term resilience means that people develop cognitive, psychological, emotional, and behavioral capabilities and social connections that enable them to calm their body, mind, emotions, and behaviors during toxic stresses or traumatic experiences in ways that enable them to\u2014 (A) respond without negative consequences for themselves or others; and (B) use the experiences as catalysts to develop a constructive new sense of meaning, purpose, and hope. (8) The term toxic stress means exposure to prolonged, severe, and stressful situations with no period of recovery or support. (g) Authorization of appropriations (1) In general To carry out this section, there is authorized to be appropriated $36,000,000 for the period of fiscal years 2025 through 2029. (2) Limitation Of the amount made available to carry out this section for a fiscal year, not more than 5 percent of such funds may be used to carry out subsection (d). .",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2445",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Community Mental Wellness and Resilience Act of 2025",
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
        "updateDate": "2025-09-16T13:45:02Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4744ih.xml"
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
      "title": "Community Mental Wellness and Resilience Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Mental Wellness and Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to promote mental wellness and resilience and prevent and heal mental health, behavioral health, and psychosocial conditions through developmentally and culturally appropriate community programs, and award grants for the purpose of establishing, operating, or expanding community-based mental wellness and resilience programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:22Z"
    }
  ]
}
```
