# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3420
- Title: Commitment to Aid Workers Act
- Congress: 119
- Bill type: S
- Bill number: 3420
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2026-01-06T20:03:01Z
- Update date including text: 2026-01-06T20:03:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3420",
    "number": "3420",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Commitment to Aid Workers Act",
    "type": "S",
    "updateDate": "2026-01-06T20:03:01Z",
    "updateDateIncludingText": "2026-01-06T20:03:01Z"
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
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
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
          "date": "2025-12-10T19:52:14Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3420is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3420\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Van Hollen (for himself, Mr. Merkley , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo establish a Special Envoy for Humanitarian Aid Workers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Commitment to Aid Workers Act .\n#### 2. Special Envoy for Humanitarian Aid Workers\nSection 1 of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a ) is amended by adding at the end the following:\n(p) Special Envoy for Humanitarian Aid Workers (1) Definitions In this subsection: (A) Aid worker The term aid worker means an individual who provides humanitarian assistance to people in need outside the United States. (B) Appropriate congressional committees The term appropriate congressional committees means\u2014 (i) the Committee on Appropriations of the Senate ; (ii) the Committee on Foreign Relations of the Senate ; (iii) the Committee on Appropriations of the House of Representatives ; and (iv) the Committee on Foreign Affairs of the House of Representatives . (2) Establishment There shall be a Special Envoy for Humanitarian Aid Workers (referred to in this subsection as the Special Envoy ), who shall\u2014 (A) be appointed by the President; and (B) report to the Secretary of State. (3) Rank and status of ambassador The Special Envoy shall have the rank and status of ambassador. (4) Duties The Special Envoy shall be responsible for\u2014 (A) inquiring into the death, fatal injury, or detention of any aid worker in the course of providing assistance as part of a humanitarian mission supported by the United States; (B) advocating for the robust coordination and deconfliction between humanitarian missions supported by the United States, international bodies, and relevant foreign security forces; (C) advocating for foreign countries to adopt best practices, including security for aid workers, to enable nongovernmental organizations to freely deliver humanitarian aid and assistance; (D) developing and advocating, in consultation with the Secretary of State, best practices for foreign countries to work with humanitarian nongovernmental organizations and civil society organizations; and (E) advocating for any other matter that supports the efforts of nongovernmental organizations to provide humanitarian assistance without the interference of the security of a foreign country. (5) Annual report to Congress Not later than 1 year after the date of the enactment of this subsection, and annually thereafter, the Special Envoy shall submit a report to the appropriate congressional committees regarding the working environment of the conflict areas in which aid workers operate to provide humanitarian assistance as part of a humanitarian mission supported by the United States, including\u2014 (A) any security challenges that nongovernmental organizations face in providing United States humanitarian assistance; (B) the effectiveness of the United Nations Office for the Coordination of Humanitarian Affairs in deconflicting between nongovernmental organizations providing humanitarian assistance and parties to conflict; (C) how much humanitarian assistance the United States has distributed during the preceding 1-year period; and (D) any policy recommendations. (6) Report on united nations office for the coordination of humanitarian affairs Not later than 1 year after the date of the enactment of this subsection, the Special Envoy, in consultation with the Secretary of State, shall submit a report to the appropriate congressional committees regarding the effectiveness of the efforts of the United Nations Office for the Coordination of Humanitarian Affairs with respect to coordination and deconfliction between humanitarian nongovernmental organizations and foreign countries as part of a humanitarian response supported by the United States. .\n#### 3. Investigations into any killing or fatal injury of humanitarian aid workers\nChapter 1 of part III of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2351 et seq. ) is amended by adding at the end the following:\n620N. Prohibition on assistance to countries that unlawfully kill or fatally injure humanitarian aid workers (a) Definitions In this section: (1) Active humanitarian aid mission The term active humanitarian aid mission means an ongoing, organized effort outside the United States through which United States humanitarian assistance is being delivered or administered by the international community, individual countries, or international organizations\u2014 (A) to prevent and control nonpolitical and nonmilitary crises; and (B) to mitigate the effects of such crises. (2) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Appropriations of the Senate ; (B) the Committee on Foreign Relations of the Senate ; (C) the Committee on Appropriations of the House of Representatives ; and (D) the Committee on Foreign Affairs of the House of Representatives . (3) Humanitarian aid worker The term humanitarian aid worker means an individual who is participating in an active humanitarian aid mission to provide assistance and resources to people in need. (4) Unlawful killing The term unlawful killing means the use of lethal force by a government or its agents that\u2014 (A) if in a state of armed conflict, is inconsistent with the requirements of international humanitarian law that are enshrined as principles in the Department of Defense Law of War Manual; or (B) if outside of a state of armed conflict, would constitute murder or manslaughter (as such terms are defined in sections 1111 and 1112 of title 18, United States Code). (b) Prohibition on assistance to countries that unlawfully kill or fatally injure humanitarian aid workers (1) In general No security assistance (as defined in section 502B(d)(2)) and no defense article or defense service subject to the requirements under section 36 of the Arms Export Control Act ( 22 U.S.C. 2776 ) may be furnished to any foreign country if the Secretary of State certifies to the appropriate congressional committees that such foreign country has unlawfully killed or fatally injured humanitarian aid workers or refused reasonable requests to furnish relevant information to the Secretary of the United States, unless the Secretary also certifies to the appropriate congressional committees that, in the determination of the Secretary, such foreign country\u2014 (A) has taken sufficient action to investigate previous violations, adopt corrective actions, take effective steps to bring the responsible members of the security force unit to justice, and coordinate active humanitarian aid missions; and (B) will enable humanitarian aid workers to participate in such missions without being unlawfully killed or fatally injured. (2) Applicability A certification described in paragraph (1) shall be submitted not later than 15 days before such certification takes effect. (c) Aid Worker Independent Inquiry Group (1) Establishment Not later than 60 days after the appointment of the Special Envoy for Humanitarian Aid Workers pursuant to section 1(b)(2)(A) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2651a(b)(2)(A) ) (referred to in this subsection as the Special Envoy ), the President shall establish the Aid Worker Independent Inquiry Group (referred to in this section as the Group ) to assess and analyze the death or detention of any individual participating in an active humanitarian aid mission after the date of the enactment of this section. (2) Membership The Group shall be led by the Special Envoy and consist of such number of representatives as the Special Envoy may determine appropriate from\u2014 (A) the Department of Justice; (B) the Department of State, including\u2014 (i) relevant embassies; (ii) the Office of Foreign Assistance; and (iii) relevant offices under the Undersecretary for Political Affairs; (C) the Federal Bureau of Investigation; (D) the Office of the Director of National Intelligence; and (E) any other Federal department or agency the Special Envoy determines appropriate. (3) Incident reports to congress Not later than 90 days after a death or detention described in paragraph (1) (or not later than 45 days after such death or detention if the victim is a United States citizen), the Special Envoy, in coordination with the Group, shall submit a report to Congress that includes\u2014 (A) the cause of such death or detention; (B) with respect to a death\u2014 (i) a description of the events leading up to such death; (ii) if the military of a foreign country is responsible for causing the death of any such aid worker; (iii) an assessment of the circumstances surrounding such death, including the information available to and intentions of the unit of such military involved; (iv) information on the source of such death, including the type of munitions used in connection with such death, if any; (v) whether it is more likely than not that any defense article used was transferred from the United States or purchased by the perpetrator from United States assistance; and (vi) any other detail that the Special Envoy determines relevant to the circumstances of the death; (C) with respect to a detention, information on the grounds for such detention, including any criminal charges and evidence against the detainee; (D) an assessment of the degree of cooperation with the investigation of the death or detention by the relevant foreign country, including whether such country has furnished all requested information; and (E) a final assessment as to whether such death or detention was consistent with the laws of the international community, of the host country, and the Department of Defense Law of War Manual. .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in Senate"
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T20:03:00Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3420is.xml"
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
      "title": "Commitment to Aid Workers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Commitment to Aid Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Special Envoy for Humanitarian Aid Workers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:37Z"
    }
  ]
}
```
