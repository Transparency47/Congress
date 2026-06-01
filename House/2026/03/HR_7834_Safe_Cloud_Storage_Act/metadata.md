# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7834
- Title: Safe Cloud Storage Act
- Congress: 119
- Bill type: HR
- Bill number: 7834
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-04-03T15:02:51Z
- Update date including text: 2026-04-03T15:02:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7834",
    "number": "7834",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Safe Cloud Storage Act",
    "type": "HR",
    "updateDate": "2026-04-03T15:02:51Z",
    "updateDateIncludingText": "2026-04-03T15:02:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
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
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:06:10Z",
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
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "PA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "TN"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7834ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7834\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2026 Ms. Lee of Florida (for herself, Ms. Dean of Pennsylvania , Mr. Cohen , and Mr. Knott ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo limit liability for certain entities storing child sexual abuse material for law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safe Cloud Storage Act .\n#### 2. Storage of child pornography and child obscenity\n##### (a) In general\nTitle II of the PROTECT Our Children Act of 2008 ( 34 U.S.C. 21101 et seq. ) is amended by inserting after section 201 the following:\n202. Modernizing law enforcement's ability to store child pornography and child obscenity and limited liability for approved vendors (a) Definitions In this section: (1) Approved vendor The term approved vendor means an organization, corporation, or entity that\u2014 (A) offers digital storage services, including remote or cloud-based storage, and analytical and forensic tool processing support; and (B) has been contractually retained by a covered agency to support the duties of such agency by\u2014 (i) storing digital child pornography or child obscenity; (ii) making such child pornography or child obscenity available to the contracting agency, or any law enforcement or prosecutorial agency designated by the contracting agency, upon request; and (iii) providing maintenance, technical and analytical assistance, and forensic tool processing support upon request by the contracting agency. (2) Child pornography The term child pornography has the meaning given that term in section 2256(8) of title 18, United States Code. (3) Child obscenity The term child obscenity has the meaning given that term in section 21101(2) of title 34, United States Code. (4) Covered agency The term covered agency means a United States Federal, State, or local law enforcement or prosecutorial agency. (5) Local The term local means any political subdivision of a State. (6) State The term State means any of the 50 States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands of the United States, Guam, American Samoa, or the Commonwealth of the Northern Mariana Islands. (b) Limited liability for approved vendors (1) Limited liability for law enforcement approved vendors Except as provided in paragraph (2), a civil claim or criminal charge may not be brought in any Federal or State court against an approved vendor relating to the approved vendor's performance of any contractual obligation or service described in subsection (a)(1). (2) Intentional, reckless, or other misconduct A civil claim or criminal charge may be brought in any Federal or State court against an approved vendor if the approved vendor\u2014 (A) engaged in\u2014 (i) intentional misconduct; or (ii) negligent conduct; or (B) acted, or failed to act\u2014 (i) with actual malice; (ii) with reckless disregard to a substantial risk of causing injury without legal justification; or (iii) for a purpose unrelated to the performance of any responsibility or function described in subsection (a)(1)(B). (c) Vendor cybersecurity requirements With respect to any child pornography or child obscenity stored, maintained, or processed by an approved vendor, such approved vendor shall\u2014 (1) secure such child pornography or child obscenity in a manner that is consistent with the most recent version of the Cybersecurity Framework developed by the National Institute of Standards and Technology, or any successor thereto; (2) only access the child pornography or child obscenity upon consent of the law enforcement or prosecutorial agency contracting the service and for the purpose of providing maintenance, technical assistance, and forensic tool processing support in the cloud; (3) minimize the number of employees that may be able to obtain access to such child pornography or child obscenity and maintain a list of employees who have obtained such access; (4) employ end-to-end encryption for data storage and transfer functions, or an equivalent technological standard; (5) undergo an independent annual cybersecurity audit to determine whether such child pornography or child obscenity is secured as required by paragraph (1), including by assessing compliance with the National Institute of Standards and Technology Special Publication 800\u201353, Revision 5 (relating to security and privacy controls for information systems and organizations) or any successor documents or revisions; and (6) promptly address all issues identified by an audit described in paragraph (5). (d) Evidence storage Any covered agency that stores child pornography and child obscenity pursuant to a contract with an approved vendor shall retain such evidence\u2014 (1) in compliance with the security policy of the Criminal Justice Information Services Division of the Federal Bureau of Investigation, or any other similar and appropriate division within the Federal Bureau of Investigation; (2) for a period consistent with the evidence retention requirements applicable to the investigating or prosecuting covered agency under the relevant Federal, State, or local law, rule of criminal procedure, or prosecutorial policy; or (3) in the absence of such law, rule, or policy, for a period not less than the applicable statute of limitations or the duration of any sentence imposed, including the period of post-conviction review. (e) Additional requirements for approved vendors (1) Location of data (A) In general Except as provided in subparagraph (B), each approved vendor shall ensure that child pornography and child obscenity stored pursuant to this section remains in the United States. (B) Exception Child pornography and child obscenity under this section may be transferred outside the United States only with the express consent of the contracting covered agency if such agency deems the transfer necessary for investigative purposes. (2) Notification letter (A) In general Approved vendors shall file a notification letter with the Criminal Division of the Department of Justice not later than 30 days after entering into a contract described in subsection (a)(1)(B). (B) Contents The notification letter described in subparagraph (A) shall include the entity name and point of contact information of the approved vendor, the name of the contracting covered agency, the period of performance of the contract, and an acknowledgment by the approved vendor that the approved vendor will notify the Child Exploitation and Obscenity Section of the Criminal Division of the Department of Justice of any changes to the information in the letter. (3) Breach of contract (A) In general If a covered agency fails to make required payment under a contract, breaches any material term of such contract, or otherwise terminates such contract without establishing lawful transfer of the evidence, the approved vendor shall, not later than 30 days after the failure, breach, or termination, notify the Criminal Division of the Department of Justice in the case of a breach by a Federal agency, or the appropriate State attorney general in the case of a breach by a State or local agency. (B) Maintenance of evidence Upon making a notification under subparagraph (A), the approved vendor shall continue to preserve and maintain the integrity of the evidence until a prompt and lawful transfer of custody occurs to the Criminal Division of the Department of Justice or another Federal, State, or local law enforcement agency with jurisdiction. (f) Rule of construction Nothing in this section shall be construed to limit\u2014 (1) bona fide use by the contracting covered agency of child pornography or child obscenity being stored by the approved vendor, which includes providing such child pornography or child obscenity to any other party as necessary for an investigation or prosecution; or (2) the obligation of the contracting covered agency to comply with a constitutional or statutory obligation, court order, or request from a victim made pursuant to section 3509(m)(3) of title 18, United States Code. .\n##### (b) Clerical amendment\nSection 1(b) of the PROTECT Our Children Act of 2008 ( Public Law 110\u2013401 ; 122 Stat. 4229) is amended by inserting after the item relating to section 201 the following:\nSec. 202. Modernizing law enforcement's ability to store child pornography and child obscenity and limited liability for approved vendors. .",
      "versionDate": "2026-03-05",
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
        "actionDate": "2026-02-24",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 345."
      },
      "number": "3023",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Safe Cloud Storage Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-01T17:56:46Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7834ih.xml"
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
      "title": "Safe Cloud Storage Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T04:58:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Cloud Storage Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T04:58:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit liability for certain entities storing child sexual abuse material for law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T04:48:27Z"
    }
  ]
}
```
