# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1299
- Title: EAGLES Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1299
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-30T08:06:38Z
- Update date including text: 2026-04-30T08:06:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1299",
    "number": "1299",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "D000600",
        "district": "26",
        "firstName": "Mario",
        "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
        "lastName": "Diaz-Balart",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "EAGLES Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:38Z",
    "updateDateIncludingText": "2026-04-30T08:06:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:03:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AZ"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "FL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "KS"
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
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "NY"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "VA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "WA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NE"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NJ"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CO"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "MN"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "FL"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "FL"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1299ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1299\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Diaz-Balart (for himself and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 18, United States Code, to reauthorize and expand the National Threat Assessment Center of the Department of Homeland Security.\n#### 1. Short title\nThis Act may be cited as the EAGLES Act of 2025 .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nOn February 14, 2018, 17 individuals were murdered in a senseless and violent attack on Marjory Stoneman Douglas High School in Parkland Florida, a school whose mascot is the eagle.\n**(2)**\nThese individuals\u2014Alaina Petty, Alex Schachter, Alyssa Alhadeff, Cara Loughran, Carmen Schentrup, Gina Montalto, Helena Ramsay, Jaime Guttenberg, Joaquin Oliver, Luke Hoyer, Martin Duque, Meadow Pollack, Nicholas Dworet, Peter Wang, Aaron Feis, Chris Hixon, and Scott Beigel\u2014lived lives of warmth, joy, determination, service, and love, and their loss is mourned by the Nation.\n**(3)**\nLike many attackers, the shooter in that attack exhibited patterns of threatening and concerning behavior prior to the massacre that were alarming and that should have alerted law enforcement and other Federal, State, and local officials about the potential for violence.\n**(4)**\nActs of targeted violence, including the attack on Marjory Stoneman Douglas High School, are preventable.\n**(5)**\nLives were saved because of the brave and exemplary conduct of many students, teachers, and staff at Marjory Stoneman Douglas High School, including several of the victims of the attack.\n**(6)**\nThe Secret Service National Threat Assessment Center (referred to in this Act as the Center ) was established in 1998 to conduct research on all forms of targeted violence, including attacks targeting government officials, government facilities, workplaces, houses of worship, K\u201312 schools, universities, and mass attacks in public spaces.\n**(7)**\nResearch published by the Center on targeted violence has shown that\u2014\n**(A)**\nmost incidents were planned in advance;\n**(B)**\nthe attackers\u2019 behavior gave some indication that the individual was planning, or at least contemplating, an attack;\n**(C)**\nmost attackers had already exhibited a pattern of behavior that elicited concern to other people in their lives; and\n**(D)**\nprior to the attack, someone associated with the attacker, such as a family member or peer, often knew the attack was to likely to occur.\n**(8)**\nThrough their research, the Center developed the Secret Service\u2019s behavioral threat assessment model for preventing targeted violence, which includes a 3-step process\u2014\n**(A)**\nidentifying individuals who are exhibiting threatening or concerning behaviors that indicate they may pose a risk of violence;\n**(B)**\nassessing whether the individual poses a risk, based on articulable facts; and\n**(C)**\nrisk posed by the individualized proactive and preventive measures.\n**(9)**\nThe Secret Service\u2019s behavioral threat assessment model works most effectively when all the relevant parties, including local law enforcement, mental health professionals, workplace managers, school personnel, and members of the community, are part of a comprehensive protocol to identify, assess, and manage a potential threat.\n**(10)**\nThe primary goal of behavioral threat assessment programs is to prevent targeted violence, with an emphasis on providing early intervention and connecting individuals exhibiting threatening or concerning behavior to existing community resources for support.\n**(11)**\nEarly intervention is a proven and effective way to prevent violent conduct that would otherwise harm others and necessitate more punitive action, including criminal penalties.\n**(12)**\nThe parties involved need the appropriate research, guidance, training, and tools to establish the appropriate mechanisms for implementing this type of preventative approach.\n**(13)**\nIn K\u201312 schools, a behavioral threat assessment is a proactive approach to identify, assess, and provide age-appropriate interventions, resources, and supports for students who display behavior that elicits concerns for the safety of themselves or others.\n**(14)**\nThere has been a 79 percent decline in juvenile arrests in K\u201312 school communities who have received Center training, thus successfully diverting youth away from the criminal justice system.\n**(15)**\nThe demand from local communities throughout the United States for behavioral threat assessment trainings has significantly increased. Since its inception, the Center has provided over 2,575 training sessions to over 273,000 attendees.\n**(16)**\nFrom fiscal year 2018 to fiscal year 2022, the Center has experienced a 117 percent increase in demand for training sessions, with five times as many participants.\n**(17)**\nThe Center additionally provides consultation and follow-up engagements with government agencies, law enforcement, schools, and other organizations with public safety responsibilities. From fiscal year 2018 to fiscal year 2022 the Center has seen a 553 percent increase in consultation activities.\n##### (b) Sense of Congress\nIt is the sense of Congress that a fact-based behavioral threat assessment approach, involving local law enforcement, mental health professionals, workplace managers, school personnel, other public safety officials, and members of the community, is one of the most effective ways to prevent targeted violence impacting communities across the country, and is a fitting memorial to those whose lives were taken in the February 14, 2018, attack on Marjory Stoneman Douglas High School and those who heroically acted to preserve the lives of their friends, students, and colleagues.\n#### 3. Reauthorization and expansion of the national threat assessment center of the Department of Homeland Security\n##### (a) In general\nChapter 203 of title 18, United States Code, is amended by inserting after section 3056A the following:\n3056B. Functions of the National Threat Assessment Center of the United States Secret Service (a) In general There is established a National Threat Assessment Center (in this section referred to as the Center ), to be operated by the United States Secret Service, at the direction of the Secretary of Homeland Security. (b) Functions The functions of the Center shall include the following: (1) Training and education in the area of best practices on threat assessment and the prevention of targeted violence. (2) Consultation on complex threat assessment cases and programs. (3) Research on threat assessment and the prevention of targeted violence, consistent with evidence-based standards and existing laws and regulations. (4) Facilitation of information sharing on threat assessment and the prevention of targeted violence among agencies and organizations with protective or public safety responsibilities, as well as other public or private entities. (5) Development of evidence-based programs to promote the standardization of Federal, State, and local threat assessments and best practices for the prevention of targeted violence. (c) Safe school initiative In carrying out the functions described in subsection (b), the Center shall establish a national program on targeted school violence prevention, focusing on the following activities: (1) Research The Center shall\u2014 (A) conduct research into targeted school violence and evidence-based practices in targeted school violence prevention, including school threat assessment; and (B) publish the findings of the Center on the public website of the United States Secret Service and on the School Safety Clearinghouse website, known as www.SchoolSafety.gov. (2) Training (A) In general The Center shall develop and offer training courses on targeted school violence prevention to agencies with protective or public safety responsibilities and other public or private entities, including local educational agencies. (B) Plan Not later than one year after the date of enactment of this section, the Center shall establish a plan to offer its training and other educational resources to public or private entities within each State. (3) Coordination with other Federal agencies The Center shall develop research and training programs under this section in coordination with the Department of Justice, the Department of Education, and the Department of Health and Human Services. (4) Consultation with entities outside the Federal Government The Center is authorized to consult with State and local educational, law enforcement, and mental health officials and private entities in the development of research and training programs under this section. (5) Interactive website The Center may create an interactive website to disseminate information and data on evidence-based practices in targeted school violence prevention. (d) Hiring of additional personnel The Director of the United States Secret Service may hire additional personnel to comply with the requirements of this section, which, if the Director exercises such authority, shall include\u2014 (1) at least one employee with expertise in child psychological development; and (2) at least one employee with expertise in school threat assessment. (e) Report to Congress Not later than two years after the date of enactment of this section, the Director of the Secret Service shall submit to the Committee on the Judiciary, the Committee on Health, Education, Labor, and Pensions, and the Committee on Appropriations of the Senate and the Committee on the Judiciary, the Committee on Education and Labor, and the Committee on Appropriations of the House of Representatives a report on actions taken by the United States Secret Service to implement provisions of this section, which shall include information relating to the following: (1) The number of employees hired (on a full-time equivalent basis). (2) The number of individuals in each State trained in threat assessment. (3) The number of school districts in each State trained in school threat assessment or targeted school violence prevention. (4) Information on Federal, State, and local agencies trained or otherwise assisted by the Center. (5) A formal evaluation indicating whether the training and other assistance provided by the Center is effective. (6) A formal evaluation indicating whether the training and other assistance provided by the Center was implemented by the school. (7) A summary of the Center\u2019s research activities and findings. (8) A strategic plan for disseminating the Center\u2019s educational and training resources to each State. (f) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2030. (g) No funds To provide firearms training Amounts made available to carry out this section may not be used to train any person in the use of a firearm. (h) No effect on other laws Nothing in this section may be construed to preclude or contradict any other provision of law authorizing training in the use of firearms. (i) Termination This section shall terminate on September 30, 2030. (j) Definitions In this section: (1) Evidence-based The term evidence-based means\u2014 (A) strong evidence from at least one well-designed and well-implemented experimental study; (B) moderate evidence from at least one well-designed and well-implemented quasi-experimental study; or (C) promising evidence from at least one well-designed and well-implemented correlational study with statistical controls for selection bias. (2) Local educational agency The term local educational agency has the meaning given such term under section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ); and (3) State The term State means any State of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands. .\n##### (b) Technical, conforming, and clerical amendments\n**(1) Technical and conforming amendment**\nSection 4 of the Presidential Threat Protection Act of 2000 ( 18 U.S.C. 3056 note) is repealed.\n**(2) Clerical amendment**\nThe table of sections for chapter 203 of title 18, United States Code, is amended by inserting after the item relating to section 3056A the following new item:\n3056B. Functions of the National Threat Assessment Center of the United States Secret Service. .",
      "versionDate": "2025-02-13",
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
        "actionDate": "2025-02-13",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "560",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "EAGLES Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-13T19:08:49Z"
          },
          {
            "name": "Department of Homeland Security",
            "updateDate": "2025-06-13T19:07:48Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-06-13T19:08:36Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-13T19:08:19Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-13T19:08:08Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-13T19:08:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-13T19:08:31Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-13T19:08:55Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-13T19:08:24Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-06-13T19:08:04Z"
          },
          {
            "name": "Protection of officials",
            "updateDate": "2025-06-13T19:07:56Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-06-13T19:08:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T13:47:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1299",
          "measure-number": "1299",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1299v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>"
        },
        "title": "EAGLES Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1299.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr1299"
    },
    "title": "EAGLES Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>EAGLES Act of 2025</strong></p><p>This bill reauthorizes the National Threat Assessment Center (NTAC) within the U.S. Secret Service.</p><p>It reauthorizes the functions of NTAC through FY2030 and expands them to include additional activities related to the prevention of targeted violence, such as the establishment of a national program on targeted school violence prevention.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119hr1299"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1299ih.xml"
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
      "title": "EAGLES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EAGLES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to reauthorize and expand the National Threat Assessment Center of the Department of Homeland Security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:32Z"
    }
  ]
}
```
