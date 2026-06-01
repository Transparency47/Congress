# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5116
- Title: Empower Parents to Protect their Kids Act
- Congress: 119
- Bill type: HR
- Bill number: 5116
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-01-21T09:05:36Z
- Update date including text: 2026-01-21T09:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5116",
    "number": "5116",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001211",
        "district": "15",
        "firstName": "Mary",
        "fullName": "Rep. Miller, Mary E. [R-IL-15]",
        "lastName": "Miller",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Empower Parents to Protect their Kids Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:36Z",
    "updateDateIncludingText": "2026-01-21T09:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
    },
    {
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "SC"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "CO"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "NC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "AL"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TN"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "NY"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "SC"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "LA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "WI"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MS"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "NC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "sponsorshipWithdrawnDate": "2026-01-20",
      "state": "PA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "SC"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5116ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5116\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mrs. Miller of Illinois (for herself, Mrs. Luna , Mrs. Biggs of South Carolina , Mr. Self , Ms. Boebert , Mr. Harrigan , Mr. Moore of Alabama , Mrs. Harshbarger , Ms. Stefanik , and Ms. Mace ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require elementary schools and secondary schools that receive Federal funds to obtain parental consent before facilitating a child\u2019s gender transition in any form, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Empower Parents to Protect their Kids Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSchool districts across the country have violated parental and familial rights by encouraging or instructing staff to deceive or withhold information from parents if their child expresses discomfort with their sex or is seeking to socially or physically adopt an identity that is incongruent with their sex. Without parental knowledge or consent, schools are changing the names and pronouns of children in school, provided or allowed students to bring clothes typically worn by the opposite sex for students to change into once they arrive at school, or even allowing children to change which sex-segregated facilities they use, such as rest rooms, locker rooms, and dormitories or other housing for overnight field trips.\n**(2)**\nThis is often being done pursuant to a gender transition plan that is nearly always kept secret from parents. In fact, these school districts have kept a second set of student records that are unknown to the parents. Powerful teachers unions and activist organizations have pressured more schools to adopt policies to enable and encourage children, of any age, to adopt an identity that is incongruent with their sex and be treated accordingly at school without parental notice or consent.\n**(3)**\nContrary to the unfounded assertions of activists, the social aspects of adopting an identity that is incongruent with an individual\u2019s sex are not neutral or uncontroversial. This is experimental and has immediate effects on a child\u2019s psychology and dramatically increases the statistical likelihood that a child will go on to take puberty blocking or suppressing drugs and wrong-sex hormones. Additionally, it makes it more difficult for a child to reverse course later on, thereby increasing the likelihood that the child will continue on to the surgical elements of adopting an identity that is incongruent with one\u2019s sex, resulting in life-changing, irreversible consequences.\n**(4)**\nAny policies that attempt to circumvent parental authority are a violation of parents\u2019 constitutionally protected rights to direct the care, custody, and upbringing of their children as recognized by the Supreme Court. Further, policies that withhold information from parents or ask children about intimate details of their family life violate Federal statutes designed to uphold a parent\u2019s rights and duties in education. School districts implementing such policies are misrepresenting or entirely ignoring these statutes and constitutional protections.\n**(5)**\nOn January 29, 2025, President Trump signed Executive Order 14191 Ending Radical Indoctrination in K\u201312 Schooling , to enforce the law to ensure that recipients of Federal funds providing K\u201312 education comply with all laws protecting parental rights.\n**(6)**\nSchools should never be allowed to intrude on family life by misleading or excluding parents and confusing children.\n#### 3. Requirements of parental consent\n##### (a) In general\nNo Federal funds shall be made available to any elementary school or secondary school unless the elementary school or secondary school, with respect to students enrolled at the school who have not yet reached 18 years of age, complies with each of the following requirements:\n**(1)**\nSchool employees do not proceed with any accommodation intended to affirm a student\u2019s purported identity that is incongruent with the student\u2019s sex, or any action to facilitate or otherwise aid and abet a minor in adopting such an identity, including referral or recommendation to any third-party medical provider for a gender transition procedure, unless the employees have received express parental consent to do so.\n**(2)**\nSchool employees do not facilitate, encourage, or coerce students to withhold information from their parents regarding the student\u2019s purported identity, when it is incongruent with the student\u2019s sex.\n**(3)**\nSchool employees do not withhold or hide information from parents about a student\u2019s discomfort with their sex, their desire for an identity that is incongruent with their sex, their profession of an identity that is incongruent with their sex, or their desire to undergo a gender transition procedure.\n**(4)**\nSchool employees do not encourage, pressure, or coerce the parents of students, or students themselves, to proceed with any intervention to affirm the student\u2019s adoption of an identity that is incongruent with their sex.\n##### (b) Rules of construction\nNothing in this section shall be construed\u2014\n**(1)**\nto prevent a school employee from contacting appropriate legal authorities about an imminent threat to a student\u2019s physical safety in the event that the school employee knows or has a reasonable suspicion that the student is at risk of physical abuse, as defined in section 1169 of title 18, United States Code; or\n**(2)**\nto deprive any parent of the right to be involved in a child\u2019s actions or discussions about gender transition, without the due process of law.\n##### (c) Ensuring compliance\nThe head of each Federal agency shall require each application for Federal assistance submitted by a State educational agency or local educational agency to the head of such Federal agency\u2014\n**(1)**\nto describe the steps that each elementary school and secondary school served by the State educational agency or local educational agency proposes to take to ensure compliance with the requirements under this section and how these steps preserve and protect the authority of the family; and\n**(2)**\nto ensure that\u2014\n**(A)**\na copy of the written policy that each elementary school and secondary school served by the State educational agency or local educational agency has to ensure compliance with the requirements under this section is provided to the head of such Federal agency and to the families of enrolled students; and\n**(B)**\neach such policy is clearly and publicly posted on the website of the school.\n##### (d) Civil action for certain violations\n**(1) In general**\nA qualified party may, in a civil action, obtain appropriate relief with regard to a designated violation.\n**(2) Administrative remedies not required**\nAn action under this section may be commenced, and relief may be granted, without regard to whether the party commencing the action has sought or exhausted any available administrative remedy.\n**(3) Defendants in actions under this section may include governmental entities as well as others**\nAn action under this section may be brought against any elementary school or secondary school receiving Federal financial assistance or any governmental entity assisting an elementary school or secondary school.\n**(4) Nature of relief**\nIn an action under this section, the court shall grant\u2014\n**(A)**\nall appropriate relief, including injunctive relief and declaratory relief;\n**(B)**\nto a prevailing plaintiff, reasonable attorneys\u2019 fees and litigation costs; and\n**(C)**\npayment for treatments or therapy to repair harm to the child from pursuit of gender transition determined as necessary by the parent and the child\u2019s medical providers.\n**(5) Attorneys fees for defendant**\nIf a defendant in a civil action under this subsection prevails and the court finds that the plaintiff\u2019s suit was frivolous, the court shall award a reasonable attorney\u2019s fee in favor of the defendant against the plaintiff.\n##### (e) Definitions\nIn this section:\n**(1) Female**\nThe term female , when used to refer to a natural person, means an individual who naturally has, had, will have, or would have, but for a congenital anomaly, historical accident, or intentional or unintentional disruption, the reproductive system that at some point produces, transports, and utilizes eggs for fertilization.\n**(2) Male**\nThe term male , when used to refer to a natural person, means an individual who naturally has, had, will have, or would have, but for a congenital anomaly, historical accident, or intentional or unintentional disruption, the reproductive system that at some point produces, transports, and utilizes sperm for fertilization.\n**(3) Sex**\nThe term sex , when referring to an individual\u2019s sex, means to refer to either male or female, as biologically determined.\n**(4) Designated violation**\nThe term designated violation means an actual or threatened violation of this section.\n**(5) ESEA**\nThe term elementary school and secondary school have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(6) Gender transition**\nThe term gender transition means the process in which an individual goes from identifying with or presenting as his or her sex to identifying with or presenting a self-proclaimed identity that does not correspond with or is different from his or her sex, and may be accompanied with social, legal, or physical changes.\n**(7) Governmental entity**\nThe term governmental entity, means a school district, a local educational agency, a school board, or any agency or other governmental unit or subdivision of a State responsible for education, or of such a local government.\n**(8) Qualified party**\nThe term qualified party means\u2014\n**(A)**\nthe Attorney General of the United States; or\n**(B)**\nany parent or legal guardian adversely affected by the designated violation.",
      "versionDate": "2025-09-03",
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
        "actionDate": "2025-09-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Empower Parents to Protect their Kids Act of 2025",
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
        "name": "Education",
        "updateDate": "2025-09-23T11:47:37Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5116ih.xml"
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
      "title": "Empower Parents to Protect their Kids Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Empower Parents to Protect their Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require elementary schools and secondary schools that receive Federal funds to obtain parental consent before facilitating a child's gender transition in any form, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:03:26Z"
    }
  ]
}
```
