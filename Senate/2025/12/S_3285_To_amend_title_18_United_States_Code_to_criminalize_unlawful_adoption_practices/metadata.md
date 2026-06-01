# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3285?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3285
- Title: ADOPT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3285
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-02-06T12:03:17Z
- Update date including text: 2026-02-06T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3285",
    "number": "3285",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "ADOPT Act of 2025",
    "type": "S",
    "updateDate": "2026-02-06T12:03:17Z",
    "updateDateIncludingText": "2026-02-06T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-01",
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
            "date": "2025-12-01T21:44:26Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-01T21:44:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-12-01",
      "state": "AL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "TN"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "ND"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "HI"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-05",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3285is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3285\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Ms. Klobuchar (for herself, Mrs. Britt , Mr. Blumenthal , Mrs. Blackburn , Mr. Cramer , Ms. Hirono , and Mr. Husted ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to criminalize unlawful adoption practices.\n#### 1. Short title\nThis Act may be cited as the Adoption Deserves Oversight, Protection, and Transparency Act of 2025 or the ADOPT Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to\u2014\n**(1)**\nprotect individuals and families impacted by private domestic interstate adoption from exploitation by unlicensed adoption intermediaries;\n**(2)**\nensure that individuals seeking assistance with private domestic interstate adoption have ready access to licensed and regulated adoption providers in their communities; and\n**(3)**\nprevent the commodification of children who are the subjects of private domestic interstate adoptions.\n#### 3. Adoption offense\n##### (a) In general\nChapter 11A of title 18, United States Code, is amended by adding at the end the following:\n228A. Unlawful adoption practices (a) Definitions In this section: (1) Adoption advertising The term adoption advertising means a paid advertisement, article, notice, or other paid communication published in any newspaper, magazine, or on the internet, on a billboard, over radio or television, or any public media that\u2014 (A) solicits prospective adoptive parents for the purpose of acting as a link between a placing parent and a prospective adoptive parent, or the representative, attorney, or agency of a prospective adoptive parent or placing parent, for the placement of a child for adoption; (B) solicits placing parents for the purpose of acting as a link between a placing parent and a prospective adoptive parent, or the representative, attorney, or agency of a prospective adoptive parent or placing parent, for the placement of a child for adoption; or (C) offers to disburse any thing of value, including living expenses, medical or hospital care, or any other expenses of a placing parent in connection with the birth or adoption of a child. (2) Adoption intermediary services The term adoption intermediary services means the provision of any of the following services, in exchange for direct or indirect compensation: (A) Soliciting placing parents, whether through adoption advertising or other means, for the purposes of acting as a link between a placing parent and a prospective adoptive parent, or the representative, attorney, or agency of a prospective adoptive parent or placing parent, for the placement of a child for adoption. (B) Soliciting prospective adoptive parents, whether through adoption advertising or other means, for the purpose of acting as a link between a placing parent and a prospective adoptive parent, or the representative, attorney, or agency of a prospective adoptive parent or placing parent, for the placement of a child for adoption. (C) Acting as a link between placing parents of a child and prospective adoptive parents, whether directly or through the representative, attorney, or agency of a prospective adoptive parent or placing parent, for the placement of a child for adoption. (3) Placing parent The term placing parent means a parent with legal authority to place the child for adoption. (4) Public child-placing agency The term public child-placing agency means any government child welfare agency or child protection agency that has the legal authority to place children for adoption. (5) Private licensed child-placing agency The term private licensed child-placing agency means a licensed or State approved agency that has the legal authority to place children for adoption. (b) Adoption intermediary services (1) Offense Whoever, in any circumstance described in subsection (e), knowingly provides adoption intermediary services shall be punished as provided in accordance with subsection (f). (2) Exception Paragraph (1) shall not apply to\u2014 (A) a public child-placing agency; (B) an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Act that is acting under contract by a public child-placing agency; (C) a private licensed child-placing agency; (D) an attorney licensed in the State in which the intermediary services are provided; or (E) an adoption service provider accredited or approved in accordance with title II of the Intercountry Adoption Act of 2000 ( 42 U.S.C. 14921 et seq. ) advertising provision of services through an intercountry adoption program. (c) Adoption advertising (1) Offense Whoever, in any circumstance described in subsection (e), knowingly places an adoption advertisement shall be punished in accordance with subsection (f). (2) Exception Paragraph (1) shall not apply to\u2014 (A) a public child-placing agency or private licensed child-placing agency licensed to provide services in the State in which the advertisement appears; (B) an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from taxation under section 501(a) of such Act that is acting under contract by a public child-placing agency; (C) an attorney licensed in the State in which the advertisement appears; or (D) an adoption service provider accredited or approved in accordance with title II of the Intercountry Adoption Act of 2000 ( 42 U.S.C. 14921 et seq. ) advertising an intercountry adoption program. (d) Unauthorized payments to or on behalf of a placing parent (1) Offense Whoever, in any circumstance described in subsection (e), knowingly provides any thing of value, including money, property, or services (including medical or hospital care), whether payment is made directly or indirectly for the benefit of the placing parent in connection with the birth of a child and in furtherance of an adoption in an amount exceeding $2,500, before the consultation of a placing parent with a private licensed child-placing agency or attorney licensed in the State where the placing parent resides or is located, shall be punished in accordance with subsection (f). (2) Exception Paragraph (1) shall not apply with respect to any payment made by or in cooperation with\u2014 (A) a private child-placing agency licensed in the State in which the placing parent resides or is located; (B) an attorney licensed in the State in which the placing parent resides or is located; or (C) a public agency or entity pursuant to any law or regulation, including any entitlement benefit, public assistance, or similar government support. (e) Applications For the purposes of subsections (b), (c), and (d), the circumstances under which those subsections apply are\u2014 (1) the defendant, placing parent, or prospective adoptive parent traveled in interstate or foreign commerce or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the conduct described in subsection (b), (c), or (d); (2) the defendant knowingly used a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the conduct described in subsection (b), (c), or (d); (3) the defendant knowingly made a payment, directly or indirectly, using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate commerce, in furtherance of or in connection with the conduct described in subsection (b), (c), or (d); (4) the defendant knowingly transmitted in interstate or foreign commerce any communication using any means, channel, or facility, or instrumentality of interstate or foreign commerce, including wire or computer, in furtherance of or in connection with the conduct described in subsection (b), (c), or (d); (5) the conduct described in subsection (b), (c), or (d) occurred within the territorial jurisdiction of the United States, or any territory or possession of the United States; or (6) the conduct described in subsection (b) otherwise occurred in or affected interstate or foreign commerce. (f) Penalty Whoever violates subsection (b), (c), or (d)\u2014 (1) in the case of an individual, shall be fined $50,000, imprisoned for not more than 5 years, or both per violation; or (2) in the case of an organization, shall be fined $100,000 per violation. (g) Rule of construction Nothing in this section may be construed to\u2014 (1) affect the application of the Indian Child Welfare Act of 1978 ( 25 U.S.C. 1901 et seq. ); (2) limit the provision of intercountry adoption programs and services authorized under the Intercountry Adoption Act of 2000 ( 42 U.S.C. 14901 et seq. ); or (3) prohibit a State or local government from enacting or enforcing requirements that are more stringent than the requirements established under this section. .\n##### (b) Clerical amendments\n**(1) Table of chapters**\nThe table of chapters for part I of title 18, United States Code, is amended by adding at the end the following:\n11A. Child support and unlawful adoption practices 228 .\n**(2) Chapter heading**\nThe chapter heading for chapter 11A of title 18, United States Code, is amended by inserting AND UNLAWFUL ADOPTION PRACTICES after CHILD SUPPORT .\n**(3) Table of sections**\nThe table of sections for chapter 11A of title 18, United States Code, is amended by adding after the item relating to section 228, the following:\n228A. Unlawful adoption practices. .\n#### 4. Effective date\nThis Act and the amendments made by this Act shall take effect on the date that is 120 days after the date of enactment of this Act.",
      "versionDate": "2025-12-01",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6170",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ADOPT Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-18T17:00:44Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3285is.xml"
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
      "title": "ADOPT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ADOPT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Adoption Deserves Oversight, Protection, and Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 18, United States Code, to criminalize unlawful adoption practices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:33:37Z"
    }
  ]
}
```
