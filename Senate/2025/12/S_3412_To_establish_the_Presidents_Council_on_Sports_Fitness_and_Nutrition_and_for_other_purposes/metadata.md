# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3412?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3412
- Title: Presidential Fitness Test Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3412
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2026-04-17T15:20:17Z
- Update date including text: 2026-04-17T15:20:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3412",
    "number": "3412",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Presidential Fitness Test Act of 2025",
    "type": "S",
    "updateDate": "2026-04-17T15:20:17Z",
    "updateDateIncludingText": "2026-04-17T15:20:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
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
        "item": {
          "date": "2025-12-10T16:22:08Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "AL"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "AR"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3412is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3412\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Marshall (for himself, Mrs. Britt , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish the President\u2019s Council on Sports, Fitness, and Nutrition, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Presidential Fitness Test Act of 2025 .\n#### 2. President\u2019s Council on Sports, Fitness, and Nutrition\n##### (a) Establishment\nThere is established the President\u2019s Council on Sports, Fitness, and Nutrition (referred to in this section as the Council ).\n##### (b) Membership\n**(1) Appointments**\nThe Council shall consist of up to 30 members to be appointed by the President.\n**(2) Membership**\nThe members of the Council may include representatives of relevant stakeholders.\n**(3) Terms**\nA member of the Council\u2014\n**(A)**\nshall serve for a term of 2 years;\n**(B)**\nshall be eligible for reappointment; and\n**(C)**\nmay continue to serve after the expiration of their term until the appointment of a successor.\n**(4) Chair; Vice Chair**\nThe President may designate one or more of the members of the Council to serve as the Chair or Vice Chair of the Council.\n##### (c) Functions of the Council\n**(1) In general**\nThe Council shall\u2014\n**(A)**\nadvise the President concerning progress made in carrying out the provisions of this section; and\n**(B)**\nrecommend to the President actions to accelerate such progress.\n**(2) Recommendations**\nIn carrying out this section, the Council shall recommend\u2014\n**(A)**\nstrategies for reestablishing the Presidential Fitness Test, with any appropriate improvements, as the main assessment tool for a Presidential Fitness Award;\n**(B)**\nstrategies for the development and promotion of Presidential challenges and school-based programs that reward excellence in physical education;\n**(C)**\nactions to expand opportunities at the global, national, State, and local levels for participation in sports and engagement in physical fitness;\n**(D)**\nbold and innovative fitness goals for American youth with the aim of fostering a new generation of healthy, active citizens;\n**(E)**\ncampaigns and events that elevate American sports, military readiness, and health traditions;\n**(F)**\nopportunities at the global, national, State, and local levels that expand participation in sports and emphasize the importance of an active lifestyle and good nutrition, including partnerships with professional athletes, sports organizations, player\u2019s associations, influential figures, nonprofit organizations, and community groups to inspire all Americans, among other initiatives; and\n**(G)**\nstrategies to address the growing national security threat posed by the increasing rates of childhood obesity, chronic diseases, and sedentary lifestyles, which threaten the future readiness of the United States workforce and military.\n##### (d) Administration\n**(1) Executive director**\nThe President shall designate an Executive Director of the Council who shall\u2014\n**(A)**\nmanage day-to-day operations;\n**(B)**\nserve as a liaison to the President on matters and activities pertaining to the Council; and\n**(C)**\noversee engagement with executive departments and agencies, athletic institutions, and community partners.\n**(2) Information to be furnished by departments and agencies**\nEach executive department and agency shall, to the extent permitted by law and subject to the availability of funds, furnish such information and assistance to the Council as the Council may request.\n**(3) Compensation**\nMembers of the Council shall serve without compensation but may receive travel reimbursement, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter I of chapter 57 of title 5, United States Code, subject to the availability of funds.\n**(4) Funding; administrative and technical support**\nThe Secretary of Health and Human Services shall provide such funding and administrative and technical support as the Council may require, subject to appropriations Acts.\n**(5) Subcommittees**\nThe Council may, with the approval of the President, establish subcommittees as appropriate to aid in the work of the Council.\n**(6) Seal**\nThe Council shall modify the seal of the President\u2019s Council on Physical Fitness and Sports to reflect the name of the Council as established by subsection (a).\n**(7) Federal Advisory Committee Act**\nTo the extent that chapter 10 of title 5, United States Code (known as the Federal Advisory Committee Act ), may apply to the administration of this section, any functions of the President under such chapter, except that of reporting to the Congress, shall be performed by the Secretary of Health and Human Services in accordance with the guidelines and procedures issued by the Administrator of General Services.\n##### (e) Termination\nThe Council shall terminate 2 years after the date of enactment of this Act, unless extended by the President.\n##### (f) Availability of amounts\nAmounts appropriated after the date of enactment of this Act to carry out the Presidential Youth Fitness Program may be used to establish the Presidential Fitness Test in schools in the United States.",
      "versionDate": "2025-12-10",
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
        "actionDate": "2025-09-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5480",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Make America's Youth Healthy Again Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-10",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "6604",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Presidential Fitness Test Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2026-01-07T23:16:32Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3412is.xml"
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
      "title": "Presidential Fitness Test Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Presidential Fitness Test Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the President's Council on Sports, Fitness, and Nutrition, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:39Z"
    }
  ]
}
```
