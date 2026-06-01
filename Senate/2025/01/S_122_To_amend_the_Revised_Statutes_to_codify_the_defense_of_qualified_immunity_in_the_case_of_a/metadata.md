# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/122
- Title: Qualified Immunity Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 122
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/122",
    "number": "122",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Qualified Immunity Act of 2025",
    "type": "S",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T18:39:04Z",
          "name": "Referred To"
        }
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "FL"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MS"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "OK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-01-17",
      "state": "LA"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s122is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 122\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Banks (for himself, Mr. Budd , Mr. Scott of Florida , Mrs. Blackburn , Mr. Sheehy , Mr. Crapo , Mrs. Hyde-Smith , Mr. Mullin , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend the Revised Statutes to codify the defense of qualified immunity in the case of any action under section 1979, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Qualified Immunity Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nQualified immunity is intended for all but the plainly incompetent or those who knowingly violate the law and is meant to give government officials breathing room to make reasonable mistakes of fact and law.\n**(2)**\nThe Supreme Court of the United States has observed that qualified immunity balances 2 important interests: The need to hold law enforcement officers accountable when they exercise power irresponsibly and the need to shield officers from harassment, distraction, and liability when they perform their duties reasonably.\n#### 3. Codification of qualified immunity\n##### (a) In general\nSection 1979 of the Revised Statutes ( 42 U.S.C. 1983 ) is amended\u2014\n**(1)**\nby striking Every and inserting (a) In general\u2014 Every ; and\n**(2)**\nby adding at the end the following:\n(b) Applicability to law enforcement officers (1) Definitions In this subsection: (A) Law enforcement agency The term law enforcement agency means any Federal, State, Tribal, or local public agency\u2014 (i) engaged in supervision, prevention, detection, investigation, or the incarceration of any person for any violation of law; and (ii) that has the statutory powers of arrest or apprehension. (B) Law enforcement officer The term law enforcement officer \u2014 (i) means any Federal, State, Tribal, or local official who\u2014 (I) is authorized by law to engage in or supervise the prevention, detection, investigation, or the incarceration of any person for any violation of law; and (II) has the statutory powers of arrest or apprehension; and (ii) includes police officers and other agents of a law enforcement agency. (2) No liability (A) Law enforcement officers A law enforcement officer subject to an action under this section in their individual capacity shall not be found liable if such law enforcement officer establishes that\u2014 (i) the right, privilege, or immunity secured by the Constitution or Federal law was not clearly established at the time of their deprivation by the law enforcement officer, or that at this time, the state of the law was not sufficiently clear that any reasonable law enforcement officer would have understood that the conduct alleged constituted a violation of the Constitution or Federal law; or (ii) a court of competent jurisdiction had issued a final decision on the merits holding, without reversal, vacatur, or preemption, that the specific conduct alleged to be unlawful was consistent with the Constitution and Federal laws. (B) Law enforcement agencies and units of local government A law enforcement agency or unit of local government who employed a law enforcement officer subject to an action under subsection (a), shall not be liable for such action if the law enforcement officer\u2014 (i) is found not liable under paragraph (1); and (ii) was acting within the scope of their employment. .\n##### (b) Effective date\nThe amendments made under subsection (a) shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "503",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Qualified Immunity Act of 2025",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-03-03T17:13:08Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-03-03T17:15:06Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-03-03T17:24:37Z"
          },
          {
            "name": "Government liability",
            "updateDate": "2025-03-03T17:24:44Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-03-03T17:24:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-03-06T18:28:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s122",
          "measure-number": "122",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s122v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that any reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>"
        },
        "title": "Qualified Immunity Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s122.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that any reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s122"
    },
    "title": "Qualified Immunity Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Qualified Immunity Act of 2025</strong></p><p>This bill provides statutory authority for qualified immunity for law enforcement officers in civil cases involving constitutional violations.</p><p>Current law provides a statutory civil cause of action against state and local government actors (e.g., law enforcement officers) for violations of constitutional rights, also known as Section 1983 lawsuits. The Supreme Court has also found an implied cause of action against federal law enforcement officers in certain situations (e.g., Fourth Amendment violations), also known as <em>Bivens</em> lawsuits. However, under the judicial doctrine of qualified immunity, government officials performing discretionary duties are generally shielded from civil liability, unless their actions violate clearly established rights of which a reasonable person would have known.</p><p>The bill provides statutory authority for these principles with respect to law enforcement officers. Specifically, under the bill, law enforcement officers are entitled to qualified immunity if (1) at the time of the alleged violation, the constitutional right at issue was not clearly established or the state of the law was not sufficiently clear that any reasonable officer would have\u00a0known that the conduct was unconstitutional; or (2) a court has held that the specific conduct at issue is constitutional.</p><p>The bill applies to federal, state, and local law enforcement officers. It also specifies that law enforcement agencies and local governments may not be held liable if their officers are entitled to qualified immunity.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s122"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s122is.xml"
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
      "title": "Qualified Immunity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Qualified Immunity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Revised Statutes to codify the defense of qualified immunity in the case of any action under section 1979, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:17Z"
    }
  ]
}
```
