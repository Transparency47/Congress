# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6678?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6678
- Title: Senior Legal Hotline Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6678
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-14T09:06:05Z
- Update date including text: 2026-02-14T09:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6678",
    "number": "6678",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "T000491",
        "district": "45",
        "firstName": "Derek",
        "fullName": "Rep. Tran, Derek [D-CA-45]",
        "lastName": "Tran",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Senior Legal Hotline Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-14T09:06:05Z",
    "updateDateIncludingText": "2026-02-14T09:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:04:35Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "DC"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PR"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NV"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
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
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6678ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6678\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Tran (for himself, Ms. Norton , Mr. Hern\u00e1ndez , Mr. Lynch , Mr. Johnson of Georgia , Ms. Titus , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Older Americans Act of 1965 to authorize a national network of statewide senior legal hotlines, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Senior Legal Hotline Act of 2025 .\n#### 2. Statewide senior legal hotlines\nSubtitle B of title VII of the Older Americans Act of 1965 ( 42 U.S.C. 3058aa et seq. ) is amended by adding at the end the following:\n753. Statewide senior legal hotlines (a) Definitions In this section: (1) Eligible entity (A) In general The term eligible entity means a nonprofit organization or a partnership described in subparagraph (B) that\u2014 (i) provides legal assistance to older individuals at no cost to such individuals; and (ii) (I) operates a senior legal hotline in existence on the date on which the entity submits an application under subsection (c); or (II) demonstrates the capacity to provide legal assistance to older individuals through a statewide senior legal hotline. (B) Partnership A partnership described in this subparagraph is a partnership between\u2014 (i) multiple nonprofit organizations; or (ii) one or more nonprofit organizations with one or more State or local governments. (2) Senior legal hotline The term senior legal hotline means a program or partnership of programs that\u2014 (A) provides legal services, such as counseling, advice, advocacy, information, referrals, and other services, as appropriate, to older individuals on a broad range of civil legal issues; (B) provides such services by telephone (and may provide such services by additional forms of communication), regardless of whether such services are provided 24 hours a day and 7 days a week; (C) provides such services at no cost to the older individuals receiving such services; (D) serves older individuals with the greatest social need and greatest economic need as a target population for such services; and (E) develops partnerships with other programs and legal assistance providers to ensure that older individuals who need more extensive services, including representation, have access to such services. (3) Statewide senior legal hotline The term statewide senior legal hotline means a senior legal hotline that serves older individuals throughout a State. (b) Authorization The Assistant Secretary may award grants, on a competitive basis, to eligible entities that submit an application under subsection (c) to establish or operate a statewide senior legal hotline in accordance with the requirements under subsection (d). (c) Application process (1) In general An eligible entity seeking a grant under this section shall submit to the Assistant Secretary an application at such time, in such manner, and containing such information as the Assistant Secretary may reasonably require, including the contents described in paragraph (2). (2) Contents An application submitted under paragraph (1) shall contain, at a minimum, each of the following: (A) An identification of the State to be served by the statewide senior legal hotline. (B) A plan indicating how the eligible entity will satisfy each requirement under subsection (d) with respect to establishing or operating a statewide senior legal hotline. (C) An assurance that the eligible entity will be able to provide, from non-Federal funds, an amount equal to not less than 25 percent of the estimated amount awarded through the grant under this section. An eligible entity may use in-kind contributions to meet the matching requirement under this subparagraph. (D) A description of the certification process the eligible entity has in place to ensure that staff members of and volunteers serving the statewide senior legal hotline will have no conflict of interest (including any financial or substantive conflict of interest) in providing services through the hotline. (3) Selection The Assistant Secretary shall, in selecting eligible entities to receive a grant under this section\u2014 (A) consider\u2014 (i) the extent to which the application submitted by the eligible entity under paragraph (2) meets the requirements of such paragraph; and (ii) the demonstrated capacity of the eligible entity to administer a statewide senior legal hotline, including the experience and history of the eligible entity in delivering high-quality advice, assistance, and other legal services, to older individuals through low-cost and innovative methods; and (B) ensure that no 2 eligible entities receiving a grant under this section for a fiscal year are planning to establish or operate a statewide senior legal hotline that serves the same State for such fiscal year. (d) Requirements Each eligible entity receiving a grant under this section shall, in establishing or operating a statewide senior legal hotline supported by such grant\u2014 (1) provide for a sufficient number of appropriately trained attorneys, paralegals, other staff members, and volunteers to ensure effective delivery of the services described in subsection (a)(2)(A); (2) collaborate with the appropriate State agency, including any legal assistance developer of the State agency, and free or low-cost legal service providers throughout the State, including those who provide free legal assistance to older individuals, to maximize coordination and cost-effective delivery of legal assistance to older individuals; (3) strive to maximize coordination in the delivery of legal assistance to older individuals in the State, including legal assistance funded by the Legal Services Corporation under the Legal Services Corporation Act ( 42 U.S.C. 2996 et seq. ), legal assistance supported by a grant under part B of title III of this Act, legal assistance provided by a law school clinic, and any other legal assistance provided at no cost to the persons receiving the assistance; (4) build effective communication within the aging network operating in the State to provide coordinated assistance and referrals as appropriate; (5) establish mechanisms to make referrals for representation and other assistance beyond the scope of the hotline to\u2014 (A) other divisions or projects of the same legal aid agency of which the hotline is a division or project; (B) other legal aid agencies; (C) private attorneys, including those providing pro bono legal services; (D) providers included in the aging network operating in the State; (E) advocacy and assistance programs for older individuals; or (F) any other individuals or entities, as appropriate; and (6) conduct outreach through the aging network operating in the State, and by other means, to inform older individuals about the availability of the services provided by the hotline, specifically targeting older individuals with the greatest economic need and greatest social need. (e) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2027 through 2031. .",
      "versionDate": "2025-12-11",
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
        "name": "Social Welfare",
        "updateDate": "2026-01-08T15:17:14Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6678ih.xml"
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
      "title": "Senior Legal Hotline Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Senior Legal Hotline Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Older Americans Act of 1965 to authorize a national network of statewide senior legal hotlines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:22Z"
    }
  ]
}
```
