# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8396
- Title: ACCESS Act of 2026.
- Congress: 119
- Bill type: HR
- Bill number: 8396
- Origin chamber: House
- Introduced date: 2026-04-21
- Update date: 2026-05-01T14:19:38Z
- Update date including text: 2026-05-01T14:19:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-21: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-21: Introduced in House

## Actions

- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Introduced in House
- 2026-04-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-21",
    "latestAction": {
      "actionDate": "2026-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8396",
    "number": "8396",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "ACCESS Act of 2026.",
    "type": "HR",
    "updateDate": "2026-05-01T14:19:38Z",
    "updateDateIncludingText": "2026-05-01T14:19:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-21",
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
      "actionDate": "2026-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-21",
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
          "date": "2026-04-21T14:00:25Z",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8396ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8396\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2026 Mr. Calvert (for himself, Mr. Obernolte , Mr. Correa , and Mr. Fine ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Americans with Disabilities Act of 1990 to promote compliance through education, to clarify the requirements for demand letters, to provide for a notice and cure period before the commencement of a private civil action, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ADA Compliance for Customer Entry to Stores and Sites Act of 2026 or as the ACCESS Act of 2026. .\n#### 2. Compliance through education\n##### (a) In general\nBased on existing funding, the Disability Rights Section of the Department of Justice shall, in consultation with property owners, website owners and app developers, and representatives of the disability rights community, develop a program to educate State and local governments and property owners on effective and efficient strategies for promoting access to public accommodations for persons with a disability (as defined in section 3 of the Americans with Disabilities Act ( 42 U.S.C. 12102 )). Such program may include training for professionals such as Certified Access Specialists to provide a guidance of remediation for potential violations of the Americans with Disabilities Act.\n##### (b) Materials provided in other languages\nThe Disability Rights Section of the Department of Justice shall take appropriate actions, to the extent practicable, to make technical assistance publications relating to compliance with this Act and the amendments made by this Act available in all the languages commonly used by owners and operators of United States businesses.\n#### 3. Notice and cure period\nParagraph (1) of section 308(a) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12188(a)(1) ) is amended to read as follows:\n(1) Availability of remedies and procedures (A) In general Subject to subparagraph (B), the remedies and procedures set forth in section 204(a) of the Civil Rights Act of 1964 ( 42 U.S.C. 2000a\u20133(a) ) are the remedies and procedures this title provides to any person who is being subjected to discrimination on the basis of disability in violation of this title or who has reasonable grounds for believing that such person is about to be subjected to discrimination in violation of section 303. Nothing in this section shall require a person with a disability to engage in a futile gesture if such person has actual notice that a person or organization covered by this title does not intend to comply with its provisions. (B) Barriers to access to existing public accommodations (i) In general A civil action under section 302 or 303 based on the failure to\u2014 (I) remove an architectural barrier to access into an existing public accommodation, or (II) or any technological barrier to access to a website or mobile application, may not be commenced by a person aggrieved by such failure unless that person has complied with the requirements of clause (ii). (ii) Requirements for providing cure period The requirements of this clause are that\u2014 (I) the person has provided to the owner or operator of the accommodation a written notice specific enough to allow such owner or operator to identify the barrier; and (II) (aa) during the period beginning on the date the notice is received and ending 60 days after that date, the owner or operator fails to provide to that person a written description outlining improvements that will be made to remove the barrier; or (bb) if the owner or operator provides the written description under subclause (I), the owner or operator fails to remove the barrier or, in the case of a barrier, the removal of which requires additional time as a result of circumstances beyond the control of the owner or operator, fails to make substantial progress in removing the barrier during the period beginning on the date the description is provided and ending 60 days after that date. (C) Specification of details of alleged violation The written notice required under subparagraph (B) shall also specify in detail the circumstances under which an individual was actually denied access to a public accommodation, including\u2014 (i) the address of property or the necessary information to access the website or mobile application (including a URL or Bundle ID); (ii) whether a request for assistance in removing a barrier to access was made; and (iii) whether the barrier to access was a permanent or temporary barrier. .\n#### 4. Effective date\nThis Act and the amendments made by this Act take effect 30 days after the date of the enactment of this Act.\n#### 5. Mediation for ADA actions related to architectural barriers\nThe Judicial Conference of the United States shall, under rule 16 of the Federal Rules of Civil Procedure or any other applicable law, in consultation with property owners and representatives of the disability rights community, develop a model program to promote the use of alternative dispute resolution mechanisms, including a stay of discovery during mediation, to resolve claims of architectural barriers to access for public accommodations. To the extent practical, the Federal Judicial Center should provide a public comment period on any such proposal. The goal of the model program shall be to promote access quickly and efficiently without the need for costly litigation. The model program should include an expedited method for determining the relevant facts related to such barriers to access and steps taken before the commencement of litigation to resolve any issues related to access.\n#### 6. Study regarding WCAG 2.0 standards\nNot later than 1 year after the date of enactment of this Act, the Attorney General shall complete a study to determine whether WCAG 2.0 standards, accessibility widgets, or providing a telephone number through which members of the public can obtain the same information and services as they would on a website would all provide reasonable accommodations for individuals with disabilities who are protected by the provisions of the Americans with Disabilities Act of 1990.",
      "versionDate": "2026-04-21",
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
        "actionDate": "2026-03-26",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 8."
      },
      "number": "6453",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ADA 30 Days to Comply Act",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-04-27T20:32:01Z"
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
      "date": "2026-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8396ih.xml"
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
      "title": "ACCESS Act of 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-23T09:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCESS Act of 2026.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ADA Compliance for Customer Entry to Stores and Sites Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-23T09:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Americans with Disabilities Act of 1990 to promote compliance through education, to clarify the requirements for demand letters, to provide for a notice and cure period before the commencement of a private civil action, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-23T09:18:24Z"
    }
  ]
}
```
