# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/986?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/986
- Title: Safe Schools Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 986
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2026-04-08T15:10:42Z
- Update date including text: 2026-04-08T15:10:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/986",
    "number": "986",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Safe Schools Improvement Act",
    "type": "S",
    "updateDate": "2026-04-08T15:10:42Z",
    "updateDateIncludingText": "2026-04-08T15:10:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
        "item": [
          {
            "date": "2025-03-12T17:43:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-12T17:43:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "PA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "NH"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "VT"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "CT"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "WA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NM"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NJ"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "DE"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "RI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "MI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "MD"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s986is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 986\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Kaine (for himself, Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Mr. Booker , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Durbin , Mr. Fetterman , Mr. Hickenlooper , Ms. Hirono , Ms. Klobuchar , Mr. Markey , Mr. Merkley , Mrs. Murray , Mr. Padilla , Mr. Peters , Ms. Rosen , Mr. Sanders , Mrs. Shaheen , Ms. Smith , Mr. Warner , Ms. Warren , Mr. Welch , Mr. Wyden , and Mr. Murphy ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo address and take action to prevent bullying and harassment of students.\n#### 1. Short title\nThis Act may be cited as the Safe Schools Improvement Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nBullying and harassment foster a climate of fear and disrespect that can seriously impair the physical and psychological health of its victims and create conditions that negatively affect learning, thereby undermining the ability of students to achieve their full potential.\n**(2)**\nBullying and harassment contribute to high dropout rates, increased absenteeism, and academic underachievement.\n**(3)**\nBullying and harassment include a range of behaviors that negatively impact a student\u2019s ability to learn and participate in educational opportunities and activities that schools offer. Such behaviors can include hitting or punching, name-calling, intimidation through gestures or social exclusion, and sending insulting or offensive messages through electronic communications, such as internet sites, e-mail, instant messaging, mobile phones and messaging, telephone, or any other means.\n**(4)**\nSchools with enumerated anti-bullying and harassment policies have an increased level of reporting and teacher intervention in incidents of bullying and harassment, thereby reducing the overall frequency and number of such incidents.\n**(5)**\nStudents have been particularly singled out for bullying and harassment on the basis of their actual or perceived race, color, national origin, sex, disability status, sexual orientation, gender identity, sex characteristics (including intersex traits), or religion, among other categories.\n**(6)**\nSome young people experience a form of bullying called relational aggression or psychological bullying, which harms individuals by damaging, threatening, or manipulating their relationships with their peers, or by injuring their feelings of social acceptance.\n**(7)**\nInterventions to address bullying and harassment should incorporate evidence-based discipline policies and practices, such as Positive Behavior Interventions and Supports (PBIS) and other restorative practices that can minimize suspensions, expulsions, and other exclusionary and harmful discipline policies to ensure that students are not pushed-out or diverted to the juvenile justice system.\n**(8)**\nPerpetrators of bullying and harassment often have a history of trauma or psychological distress, or have been bullied themselves. These students, often discussed as bully-victims , require additional trauma-informed interventions and consideration.\n#### 3. Safe Schools improvement\n##### (a) In general\nTitle IV of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7101 et seq. ) is amended by adding at the end the following:\nG Safe Schools improvement 4701. Purpose The purpose of this part is to address the problem of bullying and harassment conduct of students in public elementary schools and secondary schools. 4702. Anti-bullying policies (a) Bullying In this part, the term bullying means conduct that adversely affects the ability of one or more students to participate in or benefit from the school\u2019s educational programs or activities by placing a student in fear of harm. (b) Policies A State that receives a grant under this title shall require all local educational agencies in the State to carry out the following: (1) Establish policies that prevent and prohibit conduct, including bullying and harassment, that\u2014 (A) limits a student\u2019s ability to participate in, or benefit from, a program or activity of a public school or local educational agency; or (B) creates a hostile or abusive educational environment, adversely affecting a student's education, at a program or activity of a public school or local educational agency, including acts of verbal, nonverbal, or physical aggression or intimidation. (2) The policies required under paragraph (1) shall include a prohibition of bullying or harassment conduct based on\u2014 (A) a student\u2019s actual or perceived race, color, national origin, sex (including sexual orientation, gender identity, and sex characteristics (including intersex traits)), disability, or religion; (B) the actual or perceived race, color, national origin, sex (including sexual orientation, gender identity, and sex characteristics (including intersex traits)), disability, or religion of a person with whom a student associates or has associated; or (C) any other distinguishing characteristics that may be defined by the State or local educational agency. (3) Provide\u2014 (A) annual notice to students, parents, and educational professionals describing the full range of prohibited conduct contained in such local educational agency's discipline policies; and (B) grievance procedures for students or parents to register complaints regarding the prohibited conduct contained in such local educational agency's discipline policies, including\u2014 (i) the name of the local educational agency officials who are designated as responsible for receiving such complaints; and (ii) timelines that the local educational agency will establish in the resolution of such complaints. (4) Collect annual incidence and frequency of incidents data about the conduct prohibited by the policies described in paragraph (1) at the school level that are accurate and complete and publicly report such data at the school level and local educational agency level. The local educational agency shall ensure that victims or persons responsible for such conduct are not identifiable. 4703. State reports The chief executive officer of a State that receives a grant under this title, in cooperation with the State educational agency, shall submit a biennial report to the Secretary\u2014 (1) on the information reported by local educational agencies in the State pursuant to section 4702(b)(4); and (2) describing the State's plans for supporting local educational agency efforts to address the conduct prohibited by the policies described in section 4702(b)(1). 4704. Evaluation (a) Biennial evaluation The Secretary shall conduct an independent biennial evaluation of programs and policies to combat bullying and harassment in elementary schools and secondary schools, including implementation of the requirements described in section 4702, including whether such requirements have appreciably reduced the level of the prohibited conduct and have conducted effective parent involvement and training programs. (b) Data collection The Commissioner for Education Statistics shall collect data from States, that are subject to independent review, to determine the incidence and frequency of conduct prohibited by the policies described in section 4702. (c) Biennial report Not later than January 1, 2026, and every 2 years thereafter, the Secretary shall submit to the President and Congress a report on the findings of the evaluation conducted under subsection (a) together with the data collected under subsection (b) and data submitted by the States under section 4703. 4705. Effect on other laws (a) Federal and state nondiscrimination laws Nothing in this part shall be construed to invalidate or limit rights, remedies, procedures, or legal standards available to victims of discrimination under any other Federal law or law of a State or political subdivision of a State, including title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), section 504 or 505 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 , 794a), or the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ). The obligations imposed by this part are in addition to those imposed by title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), title IX of the Education Amendments of 1972 ( 20 U.S.C. 1681 et seq. ), section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ), and the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ). (b) Free speech and expression laws Nothing in this part shall be construed to alter legal standards regarding, or affect the rights (including remedies and procedures) available to individuals under, other Federal laws that establish protections for freedom of speech or expression. 4706. Rule of construction Nothing in this part shall be construed to prohibit a State or local entity from enacting any law with respect to the prevention of bullying or harassment of students that is not inconsistent with this part. .\n##### (b) Table of contents\nThe table of contents in section 2 of the Elementary and Secondary Education Act of 1965 is amended by inserting after the item relating to section 4644 the following:\nPart G\u2014Safe Schools improvement Sec. 4701. Purpose. Sec. 4702. Anti-bullying policies. Sec. 4703. State reports. Sec. 4704. Evaluation. Sec. 4705. Effect on other laws. Sec. 4706. Rule of construction. .",
      "versionDate": "2025-03-12",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "1810",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Safe Schools Improvement Act",
      "type": "HR"
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
            "name": "Assault and harassment offenses",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Census and government statistics",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Child safety and welfare",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T15:10:42Z"
          },
          {
            "name": "Disability and paralysis",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Religion",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "School administration",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "Sex, gender, sexual orientation discrimination",
            "updateDate": "2026-02-05T21:17:49Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2026-02-05T21:17:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-31T15:48:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
    "originChamber": "Senate",
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
          "measure-id": "id119s986",
          "measure-number": "986",
          "measure-type": "s",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-05-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s986v00",
            "update-date": "2025-05-14"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safe Schools Improvement Act</strong></p><p>This bill requires states to direct their local educational agencies (LEAs) to establish policies that prevent and prohibit bullying and harassment of elementary and secondary school students. In particular, these policies must prohibit bullying and harassment based on race, color, national origin, disability, religion, or\u00a0sex. <em>Sex </em>includes\u00a0sexual orientation, gender identity, and sex characteristics (including intersex traits).</p><p>Further, LEAs must provide (1) students, parents, and educational professionals with annual notice of the conduct prohibited in their disciplinary policies; (2) students and parents with grievance procedures that target such conduct; and (3) the public with annual data on the incidence and frequency of that conduct at the school and LEA level.</p><p>The Department\u00a0of Education must conduct and report on an independent biennial evaluation of programs and policies to combat bullying and harassment in elementary and secondary schools. The National Center for Education Statistics must collect state data to determine the incidence and frequency of the conduct prohibited by LEA disciplinary policies.</p>"
        },
        "title": "Safe Schools Improvement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s986.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe Schools Improvement Act</strong></p><p>This bill requires states to direct their local educational agencies (LEAs) to establish policies that prevent and prohibit bullying and harassment of elementary and secondary school students. In particular, these policies must prohibit bullying and harassment based on race, color, national origin, disability, religion, or\u00a0sex. <em>Sex </em>includes\u00a0sexual orientation, gender identity, and sex characteristics (including intersex traits).</p><p>Further, LEAs must provide (1) students, parents, and educational professionals with annual notice of the conduct prohibited in their disciplinary policies; (2) students and parents with grievance procedures that target such conduct; and (3) the public with annual data on the incidence and frequency of that conduct at the school and LEA level.</p><p>The Department\u00a0of Education must conduct and report on an independent biennial evaluation of programs and policies to combat bullying and harassment in elementary and secondary schools. The National Center for Education Statistics must collect state data to determine the incidence and frequency of the conduct prohibited by LEA disciplinary policies.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s986"
    },
    "title": "Safe Schools Improvement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safe Schools Improvement Act</strong></p><p>This bill requires states to direct their local educational agencies (LEAs) to establish policies that prevent and prohibit bullying and harassment of elementary and secondary school students. In particular, these policies must prohibit bullying and harassment based on race, color, national origin, disability, religion, or\u00a0sex. <em>Sex </em>includes\u00a0sexual orientation, gender identity, and sex characteristics (including intersex traits).</p><p>Further, LEAs must provide (1) students, parents, and educational professionals with annual notice of the conduct prohibited in their disciplinary policies; (2) students and parents with grievance procedures that target such conduct; and (3) the public with annual data on the incidence and frequency of that conduct at the school and LEA level.</p><p>The Department\u00a0of Education must conduct and report on an independent biennial evaluation of programs and policies to combat bullying and harassment in elementary and secondary schools. The National Center for Education Statistics must collect state data to determine the incidence and frequency of the conduct prohibited by LEA disciplinary policies.</p>",
      "updateDate": "2025-05-14",
      "versionCode": "id119s986"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s986is.xml"
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
      "title": "Safe Schools Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safe Schools Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address and take action to prevent bullying and harassment of students.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:13Z"
    }
  ]
}
```
