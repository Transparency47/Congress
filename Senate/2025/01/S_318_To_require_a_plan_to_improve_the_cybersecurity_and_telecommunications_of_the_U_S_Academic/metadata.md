# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/318
- Title: ANCHOR Act
- Congress: 119
- Bill type: S
- Bill number: 318
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2026-02-04T05:06:13Z
- Update date including text: 2026-02-04T05:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 169.
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-08 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S7007-7009; text: CR S7008-7009)
- 2025-10-08 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.
- 2025-09-29 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.
- 2025-09-29 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 169.
- 2025-10-08 - Floor: Message on Senate action sent to the House.
- 2025-10-08 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S7007-7009; text: CR S7008-7009)
- 2025-10-08 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-10-10 12:33:04 - Floor: Received in the House.
- 2025-10-10 12:33:05 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/318",
    "number": "318",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "ANCHOR Act",
    "type": "S",
    "updateDate": "2026-02-04T05:06:13Z",
    "updateDateIncludingText": "2026-02-04T05:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:05",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-10-10",
      "actionTime": "12:33:04",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S7007-7009; text: CR S7008-7009)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-29",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 169.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-64.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-29",
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
            "date": "2025-09-29T19:29:15Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:03:32Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T22:38:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 318\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Padilla (for himself and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act .\n#### 2. Definitions\nIn this Act:\n**(1) U.S. Academic Research Fleet**\nThe term U.S. Academic Research Fleet means the United States-flagged vessels that\u2014\n**(A)**\nhave been accepted into, and are active participants administered within, the University-National Oceanographic Laboratory System;\n**(B)**\nare operated as oceanographic research vessels by research universities and laboratories;\n**(C)**\nreceive funding from the National Science Foundation; and\n**(D)**\nhave achieved designation as a member vessel through a standard evaluation process.\n**(2) Director**\nThe term Director means the Director of the National Science Foundation.\n**(3) Oceanographic research vessel**\nThe term oceanographic research vessel has the meaning given the term in section 2101 of title 46, United States Code.\n#### 3. Plan to improve cybersecurity and telecommunications of U.S. Academic Research Fleet\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Director shall, in consultation with the head of any Federal agency, university, or laboratory that owns or operates a vessel of the U.S. Academic Research Fleet, submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Space, Science, and Technology of the House of Representatives a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet.\n##### (b) Elements\nThe plan required by subsection (a) shall include\u2014\n**(1)**\nan assessment of the telecommunications and networking needs of the U.S. Academic Research Fleet, consistent with the typical scientific mission of that vessel;\n**(2)**\nin accordance with guidance issued by the Cybersecurity and Infrastructure Security Agency and the National Institute for Standards and Technology, an assessment of cybersecurity needs appropriate for\u2014\n**(A)**\nthe ownership of vessels within the U.S. Academic Research Fleet; and\n**(B)**\nthe typical research functions and topics of such vessels;\n**(3)**\nan assessment of the costs necessary to meet the needs described in paragraphs (1) and (2), including\u2014\n**(A)**\nany necessary equipment, such as satellite communications equipment, software, high-performance computing clusters shipboard and shoreside, or enterprise hardware; and\n**(B)**\nestimated personnel costs in excess of current expenditures, including any necessary training, support, or logistics;\n**(4)**\nan assessment of the time required to implement any upgrades required to meet the needs described in paragraphs (1) and (2) under varying budgets and funding scenarios;\n**(5)**\nthe adoption of common solutions or consortial licensing agreements, or by centralizing elements of fleet cybersecurity, telecommunications or data management at a single facility; and\n**(6)**\nin consultation with any non-Federal owners of a vessel of the U.S. Academic Research Fleet, a spending plan for the National Science Foundation, the Office of Naval Research, non-Federal owners of vessels of the U.S. Academic Research Fleet, users of the U.S. Academic Research Fleet, or any combination thereof, to provide funding to cover the costs described in paragraph (3).\n##### (c) Considerations\nThe Director shall, in preparing the plan required by subsection (a), consider\u2014\n**(1)**\nthe network capabilities, including speed and bandwidth targets, necessary to meet the scientific mission needs of each class of vessel within the U.S. Academic Research Fleet for such purposes as\u2014\n**(A)**\nexecuting the critical functions and communications of the vessel;\n**(B)**\nproviding network access for the health and well-being of deployed personnel, including communications to conduct telemedicine (including mental health care), counseling, interviews with crisis response providers, and other remote individual care and services;\n**(C)**\nas necessary to meet operations, uploading any scientific data to a shoreside server, including the copying of data off ship for disaster recovery or risk mitigation purposes;\n**(D)**\nas appropriate, conducting real-time streaming to enable shore-based observers to participate in ship-based maintenance or research activities;\n**(E)**\nreal-time coordinated viewing of\u2014\n**(i)**\nscientific instrumentation so that it is possible to conduct scientific surveys and seafloor mapping with fully remote subject-matter experts; and\n**(ii)**\ncritical operational technology by manufacturers and vendors so that it is possible to carry out maintenance and repairs to systems with limited expertise on the vessel, with fully remote subject-matter experts advising; and\n**(F)**\nas appropriate, enabling video communications to allow improved outreach to, and other educational services for, K\u201312 students, including occasional remote classroom teaching for instructors at sea to improve oceanographic access for students; and\n**(2)**\nin consultation with the Director of the Cybersecurity and Infrastructure Security Agency, the Director of the National Institute for Standards and Technology, and the heads of other Federal agencies, as appropriate\u2014\n**(A)**\nthe cybersecurity recommendations in the report of the private scientific advisory group known as JASON entitled Cybersecurity at NSF Major Facilities (JSR\u201321\u201310E) and dated October 2021 as applied to the U.S. Academic Research Fleet;\n**(B)**\naligning with international standards and guidance for information security, including the use of encryption for sensitive information, the detection and handling of security incidents, and other areas determined relevant by the Director;\n**(C)**\nfacilitating access to cybersecurity personnel and training of research and support personnel; and\n**(D)**\nthe requirements for controlled unclassified or classified information.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318rs.xml",
      "text": "II\nCalendar No. 169\n119th CONGRESS\n1st Session\nS. 318\n[Report No. 119\u201364]\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Padilla (for himself and Mr. Sullivan ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 29, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act .\n#### 2. Definitions\nIn this Act:\n**(1) U.S. Academic Research Fleet**\nThe term U.S. Academic Research Fleet means the United States-flagged vessels that\u2014\n**(A)**\nhave been accepted into, and are active participants administered within, the University-National Oceanographic Laboratory System;\n**(B)**\nare operated as oceanographic research vessels by research universities and laboratories;\n**(C)**\nreceive funding from the National Science Foundation; and\n**(D)**\nhave achieved designation as a member vessel through a standard evaluation process.\n**(2) Director**\nThe term Director means the Director of the National Science Foundation.\n**(3) Oceanographic research vessel**\nThe term oceanographic research vessel has the meaning given the term in section 2101 of title 46, United States Code.\n#### 3. Plan to improve cybersecurity and telecommunications of U.S. Academic Research Fleet\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Director shall, in consultation with the head of any Federal agency, university, or laboratory that owns or operates a vessel of the U.S. Academic Research Fleet, submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Space, Science, and Technology of the House of Representatives a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet.\n##### (b) Elements\nThe plan required by subsection (a) shall include\u2014\n**(1)**\nan assessment of the telecommunications and networking needs of the U.S. Academic Research Fleet, consistent with the typical scientific mission of that vessel;\n**(2)**\nin accordance with guidance issued by the Cybersecurity and Infrastructure Security Agency and the National Institute for Standards and Technology, an assessment of cybersecurity needs appropriate for\u2014\n**(A)**\nthe ownership of vessels within the U.S. Academic Research Fleet; and\n**(B)**\nthe typical research functions and topics of such vessels;\n**(3)**\nan assessment of the costs necessary to meet the needs described in paragraphs (1) and (2), including\u2014\n**(A)**\nany necessary equipment, such as satellite communications equipment, software, high-performance computing clusters shipboard and shoreside, or enterprise hardware; and\n**(B)**\nestimated personnel costs in excess of current expenditures, including any necessary training, support, or logistics;\n**(4)**\nan assessment of the time required to implement any upgrades required to meet the needs described in paragraphs (1) and (2) under varying budgets and funding scenarios;\n**(5)**\nthe adoption of common solutions or consortial licensing agreements, or by centralizing elements of fleet cybersecurity, telecommunications or data management at a single facility; and\n**(6)**\nin consultation with any non-Federal owners of a vessel of the U.S. Academic Research Fleet, a spending plan for the National Science Foundation, the Office of Naval Research, non-Federal owners of vessels of the U.S. Academic Research Fleet, users of the U.S. Academic Research Fleet, or any combination thereof, to provide funding to cover the costs described in paragraph (3).\n##### (c) Considerations\nThe Director shall, in preparing the plan required by subsection (a), consider\u2014\n**(1)**\nthe network capabilities, including speed and bandwidth targets, necessary to meet the scientific mission needs of each class of vessel within the U.S. Academic Research Fleet for such purposes as\u2014\n**(A)**\nexecuting the critical functions and communications of the vessel;\n**(B)**\nproviding network access for the health and well-being of deployed personnel, including communications to conduct telemedicine (including mental health care), counseling, interviews with crisis response providers, and other remote individual care and services;\n**(C)**\nas necessary to meet operations, uploading any scientific data to a shoreside server, including the copying of data off ship for disaster recovery or risk mitigation purposes;\n**(D)**\nas appropriate, conducting real-time streaming to enable shore-based observers to participate in ship-based maintenance or research activities;\n**(E)**\nreal-time coordinated viewing of\u2014\n**(i)**\nscientific instrumentation so that it is possible to conduct scientific surveys and seafloor mapping with fully remote subject-matter experts; and\n**(ii)**\ncritical operational technology by manufacturers and vendors so that it is possible to carry out maintenance and repairs to systems with limited expertise on the vessel, with fully remote subject-matter experts advising; and\n**(F)**\nas appropriate, enabling video communications to allow improved outreach to, and other educational services for, K\u201312 students, including occasional remote classroom teaching for instructors at sea to improve oceanographic access for students; and\n**(2)**\nin consultation with the Director of the Cybersecurity and Infrastructure Security Agency, the Director of the National Institute for Standards and Technology, and the heads of other Federal agencies, as appropriate\u2014\n**(A)**\nthe cybersecurity recommendations in the report of the private scientific advisory group known as JASON entitled Cybersecurity at NSF Major Facilities (JSR\u201321\u201310E) and dated October 2021 as applied to the U.S. Academic Research Fleet;\n**(B)**\naligning with international standards and guidance for information security, including the use of encryption for sensitive information, the detection and handling of security incidents, and other areas determined relevant by the Director;\n**(C)**\nfacilitating access to cybersecurity personnel and training of research and support personnel; and\n**(D)**\nthe requirements for controlled unclassified or classified information.",
      "versionDate": "2025-09-29",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 318\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act .\n#### 2. Definitions\nIn this Act:\n**(1) Director**\nThe term Director means the Director of the National Science Foundation.\n**(2) Oceanographic research vessel**\nThe term oceanographic research vessel has the meaning given the term in section 2101 of title 46, United States Code.\n**(3) U.S. Academic Research Fleet**\nThe term U.S. Academic Research Fleet means the United States flagged vessels that\u2014\n**(A)**\nhave been accepted into, and are active participants administered within, the University-National Oceanographic Laboratory System;\n**(B)**\nare operated as oceanographic research vessels by research universities and laboratories;\n**(C)**\nreceive funding from the National Science Foundation; and\n**(D)**\nhave achieved designation as a member vessel of the fleet through a standard evaluation process.\n#### 3. Plan to improve cybersecurity and telecommunications of U.S. Academic Research Fleet\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Director shall, in consultation with the head of any Federal agency, university, or laboratory that owns or operates a vessel of the U.S. Academic Research Fleet, submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Science, Space, and Technology of the House of Representatives a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet.\n##### (b) Elements\nThe plan required by subsection (a) shall include\u2014\n**(1)**\nan assessment of the telecommunications and networking needs of the U.S. Academic Research Fleet, consistent with the typical scientific missions of the vessels of such fleet;\n**(2)**\nin consultation with the Cybersecurity and Infrastructure Security Agency and the National Institute of Standards and Technology, an assessment of cybersecurity needs appropriate for\u2014\n**(A)**\nthe ownership of vessels within the U.S. Academic Research Fleet; and\n**(B)**\nthe scientific missions of such vessels;\n**(3)**\nan assessment of the costs necessary to meet the needs described in paragraphs (1) and (2), including\u2014\n**(A)**\nany necessary equipment, such as satellite communications equipment, software, high-performance computing clusters shipboard and shoreside, or enterprise hardware; and\n**(B)**\nestimated personnel costs in excess of current expenditures, including any necessary training, support, or logistics;\n**(4)**\nan assessment of the time required to implement any upgrades required to meet the needs described in paragraphs (1) and (2) under varying budgets and funding scenarios;\n**(5)**\nthe adoption of common solutions or consortial licensing agreements, or by centralizing elements of fleet cybersecurity, telecommunications, or data management at a single facility; and\n**(6)**\nin consultation with any non-Federal owners of a vessel of the U.S. Academic Research Fleet, a spending plan for the National Science Foundation, the Office of Naval Research, non-Federal owners of vessels of the U.S. Academic Research Fleet, users of the U.S. Academic Research Fleet, or any combination thereof, to provide funding to cover the costs described in paragraph (3).\n##### (c) Considerations\nThe Director shall, in preparing the plan required by subsection (a), consider\u2014\n**(1)**\nthe network capabilities, including speed and bandwidth targets, necessary to meet the scientific mission needs of each class of vessels of the U.S. Academic Research Fleet for such purposes as\u2014\n**(A)**\nexecuting the critical functions and communications of the vessels;\n**(B)**\nproviding network access to conduct medical care via telemedicine or related crisis response care;\n**(C)**\nas necessary to meet operations, uploading any scientific data to a shoreside server, including the copying of data off ship for disaster recovery or risk mitigation purposes;\n**(D)**\nas appropriate, conducting real-time streaming to enable shore-based observers to participate in ship-based maintenance or research activities; and\n**(E)**\nreal-time coordinated viewing of\u2014\n**(i)**\nscientific instrumentation so that it is possible to conduct scientific surveys and seafloor mapping with fully remote subject-matter experts; and\n**(ii)**\ncritical operational technology by manufacturers and vendors so that it is possible to carry out maintenance and repairs to systems with limited expertise on the vessel, with fully remote subject-matter experts advising; and\n**(2)**\nin consultation with the Director of the Cybersecurity and Infrastructure Security Agency, the Director of the National Institute of Standards and Technology, and the heads of other Federal agencies, as appropriate\u2014\n**(A)**\nthe cybersecurity recommendations in the report of the private scientific advisory group known as JASON entitled Cybersecurity at NSF Major Facilities (JSR\u201321\u201310E) and dated October 2021 as applied to the U.S. Academic Research Fleet;\n**(B)**\nstandards and guidance for information security, including the use of encryption for sensitive information, the detection and handling of security incidents, and other areas determined relevant by the Director;\n**(C)**\nfacilitating access to cybersecurity personnel and training of research and support personnel; and\n**(D)**\nthe requirements for controlled unclassified or classified information.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-05-22T13:27:47Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2025-05-22T13:27:47Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-05-22T13:27:47Z"
          },
          {
            "name": "National Science Foundation",
            "updateDate": "2025-05-22T13:27:47Z"
          },
          {
            "name": "Research and development",
            "updateDate": "2025-05-22T13:27:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-06T16:17:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s318",
          "measure-number": "318",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s318v00",
            "update-date": "2025-04-01"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act\u00a0</strong></p><p>This bill requires the National Science Foundation (NSF) to develop a plan to improve the cybersecurity and telecommunications capabilities of the U.S. Academic Research Fleet (ARF).</p><p>ARF is comprised of U.S.-flagged vessels that provide at-sea laboratories where oceanographic scientists, educators, and students research and learn about marine science.\u00a0</p><p>The bill requires the plan to include assessments of</p><ul><li>telecommunications and networking needs of ARF, consistent with typical scientific missions;</li><li>cybersecurity needs appropriate for the ownership of ARF vessels and their typical research functions;</li><li>the costs necessary to meet these needs; and</li><li>the time required to implement necessary upgrades.</li></ul><p>The plan must also include (1) a spending plan for the NSF, the Office of Naval Research, nonfederal\u00a0owners of ARF vessels,\u00a0and users of the vessels to cover identified costs; and (2) a proposal regarding the adoption of common solutions or\u00a0consortial licensing agreements, or the centralization of cybersecurity, telecommunications, or data management at a single facility.\u00a0</p><p>Among other factors specified in the bill, the\u00a0NSF must consider the network capabilities necessary to meet mission needs (e.g., to upload data to shoreside servers), international standards and guidance for information security, and requirements for controlled unclassified or classified information.\u00a0</p><p>The plan must be provided to Congress within one year of the bill's enactment.</p>"
        },
        "title": "ANCHOR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s318.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act\u00a0</strong></p><p>This bill requires the National Science Foundation (NSF) to develop a plan to improve the cybersecurity and telecommunications capabilities of the U.S. Academic Research Fleet (ARF).</p><p>ARF is comprised of U.S.-flagged vessels that provide at-sea laboratories where oceanographic scientists, educators, and students research and learn about marine science.\u00a0</p><p>The bill requires the plan to include assessments of</p><ul><li>telecommunications and networking needs of ARF, consistent with typical scientific missions;</li><li>cybersecurity needs appropriate for the ownership of ARF vessels and their typical research functions;</li><li>the costs necessary to meet these needs; and</li><li>the time required to implement necessary upgrades.</li></ul><p>The plan must also include (1) a spending plan for the NSF, the Office of Naval Research, nonfederal\u00a0owners of ARF vessels,\u00a0and users of the vessels to cover identified costs; and (2) a proposal regarding the adoption of common solutions or\u00a0consortial licensing agreements, or the centralization of cybersecurity, telecommunications, or data management at a single facility.\u00a0</p><p>Among other factors specified in the bill, the\u00a0NSF must consider the network capabilities necessary to meet mission needs (e.g., to upload data to shoreside servers), international standards and guidance for information security, and requirements for controlled unclassified or classified information.\u00a0</p><p>The plan must be provided to Congress within one year of the bill's enactment.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119s318"
    },
    "title": "ANCHOR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act or the ANCHOR Act\u00a0</strong></p><p>This bill requires the National Science Foundation (NSF) to develop a plan to improve the cybersecurity and telecommunications capabilities of the U.S. Academic Research Fleet (ARF).</p><p>ARF is comprised of U.S.-flagged vessels that provide at-sea laboratories where oceanographic scientists, educators, and students research and learn about marine science.\u00a0</p><p>The bill requires the plan to include assessments of</p><ul><li>telecommunications and networking needs of ARF, consistent with typical scientific missions;</li><li>cybersecurity needs appropriate for the ownership of ARF vessels and their typical research functions;</li><li>the costs necessary to meet these needs; and</li><li>the time required to implement necessary upgrades.</li></ul><p>The plan must also include (1) a spending plan for the NSF, the Office of Naval Research, nonfederal\u00a0owners of ARF vessels,\u00a0and users of the vessels to cover identified costs; and (2) a proposal regarding the adoption of common solutions or\u00a0consortial licensing agreements, or the centralization of cybersecurity, telecommunications, or data management at a single facility.\u00a0</p><p>Among other factors specified in the bill, the\u00a0NSF must consider the network capabilities necessary to meet mission needs (e.g., to upload data to shoreside servers), international standards and guidance for information security, and requirements for controlled unclassified or classified information.\u00a0</p><p>The plan must be provided to Congress within one year of the bill's enactment.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119s318"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s318es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ANCHOR Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-10-10T05:53:16Z"
    },
    {
      "title": "ANCHOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T11:03:14Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "ANCHOR Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-10-01T04:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Accelerating Networking, Cyberinfrastructure, and Hardware for Oceanic Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ANCHOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require a plan to improve the cybersecurity and telecommunications of the U.S. Academic Research Fleet, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:26Z"
    }
  ]
}
```
