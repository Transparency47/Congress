# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3981?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3981
- Title: To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals.
- Congress: 119
- Bill type: HR
- Bill number: 3981
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2026-03-30T16:29:34Z
- Update date including text: 2026-03-30T16:29:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3981",
    "number": "3981",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000590",
        "district": "3",
        "firstName": "Susie",
        "fullName": "Rep. Lee, Susie [D-NV-3]",
        "lastName": "Lee",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals.",
    "type": "HR",
    "updateDate": "2026-03-30T16:29:34Z",
    "updateDateIncludingText": "2026-03-30T16:29:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:06:45Z",
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
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "VA"
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
      "sponsorshipDate": "2025-06-24",
      "state": "PA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "AK"
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
      "sponsorshipDate": "2025-07-07",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "NC"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3981ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3981\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Ms. Lee of Nevada (for herself and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals.\n#### 1. Grant of Federal charter to Veterans Association of Real Estate Professionals\n##### (a) Grant of charter\nPart B of subtitle II of title 36, United States Code, is amended by inserting after chapter 2301 the following new chapter:\n2302 Veterans Association of Real Estate Professionals Sec. 230201. Organization. 230202. Purposes. 230203. Membership. 230204. Governing body. 230205. Powers. 230206. Restrictions. 230207. Tax-exempt status required as condition of charter. 230208. Records and inspection. 230209. Service of process. 230210. Liability for acts of officers and agents. 230211. Annual report. 230212. State defined. 230201. Organization (a) Federal charter Veterans Association of Real Estate Professionals (in this chapter, the corporation ), a nonprofit organization that meets the requirements for a veterans service organization under section 501(c)(19) of the Internal Revenue Code of 1986 and is organized under the laws of the State of California, is a federally chartered corporation. (b) Expiration of charter If the corporation does not comply with the provisions of this chapter, the charter granted by subsection (a) expires. 230202. Purposes The purposes of the corporation are those provided in its articles of incorporation and include the following: (1) To organize as a veterans service organization to maintain a continuing interest in the welfare of veterans by\u2014 (A) advocating for, and increasing sustainable homeownership; (B) providing financial literacy education, (C) spreading awareness of housing loans guaranteed by the Secretary of Veterans Affairs; and (D) increasing economic opportunities for members of the Armed Forces and veterans. (2) To establish facilities for the assistance of all veterans, with programs regarding topics including the following: (A) financial literacy (including understanding credit); (B) workforce development; (C) small business incubation and mentorship; (D) education regarding housing, including homelessness prevention, rental counseling, foreclosure prevention, and affordable housing opportunities; and (E) suicide awareness and prevention. (3) To provide a forum for real estate and financial service professionals to share ideas, learn, and be empowered to better serve the real estate needs of members of the Armed Forces, veterans, their families, and others. (4) To collaborate with organizations in the real estate & financial service sector to support employment of, and economic and business development for, veterans. 230203. Membership Eligibility for membership in the corporation, and the rights and privileges of members of the corporation, are as provided in the articles and bylaws of the corporation. 230204. Governing body (a) Board of directors The composition of the board of directors of the corporation, and the responsibilities of the board, are as provided in the articles of incorporation and bylaws of the corporation. (b) Officers The positions of officers of the corporation, and the election of the officers, are as provided in such articles of incorporation and bylaws. 230205. Powers The corporation has only those powers provided in its bylaws and articles of incorporation filed in each State in which it is incorporated. 230206. Restrictions (a) Stock and dividends The corporation may not issue stock or declare or pay a dividend. (b) Distribution of income or assets The income or assets of the corporation may not inure to the benefit of, or be distributed to, a director, officer, or member of the corporation during the life of the charter granted by this chapter. This subsection shall not prevent the payment of reasonable compensation to an officer or employee of the corporation, or reimbursement for actual necessary expenses, in amounts approved by the board of directors. (c) Political activities The corporation (or an officer of the corporation, in the course of acting in such capacity) may not contribute to, support, or participate in any political activity. (d) Loans The corporation may not make a loan to a director, officer, employee, or member of the corporation. (e) Claim of governmental approval or authority The corporation may not claim congressional approval, or the authority of the United States, for any of its activities. (f) Corporate status The corporation shall maintain its status as a corporation incorporated under the laws of the State of California. 230207. Tax-exempt status required as condition of charter If the corporation fails to maintain its status as an organization exempt from taxation under the Internal Revenue Code of 1986, the charter granted under this chapter shall terminate. 230208. Records and inspection (a) Records The corporation shall keep\u2014 (1) correct and complete records of account; (2) minutes of the proceedings of the members, board of directors, and committees of the corporation having any of the authority of the board of directors; (3) at the principal office of the corporation, a record of the names and addresses of members of the corporation entitled to vote on matters relating to the corporation; and (4) the State charter documents, bylaws, and articles of incorporation available to the public on an easily accessible website of the corporation. (b) Inspection A member entitled to vote on any matter relating to the corporation, or an agent or attorney of the member, may inspect the records of the corporation for any proper purpose, at any reasonable time. 230209. Service of process The corporation shall comply with the law of service of process of the State in which it is incorporated and each State in which it operates. 230210. Liability for acts of officers and agents The corporation is liable for the acts of its officers and agents acting within the scope of their authority. 230211. Annual report The corporation shall submit to Congress an annual report on the activities of the corporation during the preceding fiscal year. The report shall be submitted at the same time as the report of the audit required by section 10101 of this title. The report may not be printed as a public document. 230212. State defined For purposes of this chapter, the term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, or a territory or possession of the United States. .\n##### (b) Clerical amendment\nThe table of chapters at the beginning of subtitle II of title 36, United States Code, is amended by inserting after the item relating to chapter 2301 the following new item:\n2302. Veterans Association of Real Estate Professionals 230201 .",
      "versionDate": "2025-06-12",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-17T18:54:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
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
          "measure-id": "id119hr3981",
          "measure-number": "3981",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-12",
          "originChamber": "HOUSE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3981v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill grants a federal charter to the Veterans Association of Real Estate Professionals, which is a nonprofit organization that provides housing counseling to veterans and active members of the Armed Forces. </p>"
        },
        "title": "To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3981.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill grants a federal charter to the Veterans Association of Real Estate Professionals, which is a nonprofit organization that provides housing counseling to veterans and active members of the Armed Forces. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr3981"
    },
    "title": "To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals."
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill grants a federal charter to the Veterans Association of Real Estate Professionals, which is a nonprofit organization that provides housing counseling to veterans and active members of the Armed Forces. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119hr3981"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3981ih.xml"
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
      "title": "To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 36, United States Code, to grant a Federal charter to the Veterans Association of Real Estate Professionals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T03:03:29Z"
    }
  ]
}
```
