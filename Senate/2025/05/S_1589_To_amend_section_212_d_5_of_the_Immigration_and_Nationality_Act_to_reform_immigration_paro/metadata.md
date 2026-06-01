# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1589
- Title: Immigration Parole Reform Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1589
- Origin chamber: Senate
- Introduced date: 2025-05-05
- Update date: 2026-04-14T22:38:59Z
- Update date including text: 2026-04-14T22:38:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in Senate
- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-05-05: Introduced in Senate

## Actions

- 2025-05-05 - IntroReferral: Introduced in Senate
- 2025-05-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1589",
    "number": "1589",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Immigration Parole Reform Act of 2025",
    "type": "S",
    "updateDate": "2026-04-14T22:38:59Z",
    "updateDateIncludingText": "2026-04-14T22:38:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-05",
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
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T19:38:50Z",
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
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AR"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MO"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "UT"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "LA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OK"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "OH"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1589is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1589\nIN THE SENATE OF THE UNITED STATES\nMay 5, 2025 Mr. Grassley (for himself, Mr. Cotton , Mr. Hawley , Mrs. Britt , Mr. Tuberville , Mr. Budd , Mr. Lee , Ms. Ernst , Mr. Cassidy , Mr. Lankford , Mr. Moreno , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 212(d)(5) of the Immigration and Nationality Act to reform immigration parole, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Immigration Parole Reform Act of 2025 .\n#### 2. Immigration parole reform\nSection 212(d)(5) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5) ) is amended to read as follows:\n(5) (A) Except as provided in subparagraphs (B) and (C) and in section 214(f), the Secretary of Homeland Security, in the discretion of the Secretary, may temporarily parole into the United States any alien applying for admission to the United States who is not present in the United States, under such conditions as the Secretary may prescribe, on a case-by-case basis, and not according to eligibility criteria describing an entire class of potential parole recipients, for urgent humanitarian reasons or significant public benefit. Parole granted under this subparagraph may not be regarded as an admission of the alien. When the purposes of such parole have been served, in the opinion of the Secretary, the alien shall immediately return or be returned to the custody from which the alien was paroled. After such return, the case of the alien shall be dealt with in the same manner as the case of any other applicant for admission to the United States. (B) The Secretary of Homeland Security may grant parole to any alien who\u2014 (i) is present in the United States without lawful immigration status; (ii) is the beneficiary of an approved petition under section 203(a); (iii) is not otherwise inadmissible or removable; and (iv) is the spouse or child of a member of the Armed Forces serving on active duty. (C) The Secretary of Homeland Security may grant parole to any alien\u2014 (i) who is a national of the Republic of Cuba and is living in the Republic of Cuba; (ii) who is the beneficiary of an approved petition under section 203(a); (iii) for whom an immigrant visa is not immediately available; (iv) who meets all eligibility requirements for an immigrant visa; (v) who is not otherwise inadmissible; and (vi) who is receiving a grant of parole in furtherance of the commitment of the United States to the minimum level of annual legal migration of Cuban nationals to the United States specified in the U.S.\u2013Cuba Joint Communiqu\u00e9 on Migration, done at New York September 9, 1994, and reaffirmed in the Cuba-United States: Joint Statement on Normalization of Migration, Building on the Agreement of September 9, 1994, done at New York May 2, 1995. (D) For purposes of determining an alien's eligibility for parole under subparagraph (A), an urgent humanitarian reason shall be limited to circumstances in which the alien establishes that\u2014 (i) (I) the alien has a medical emergency; and (II) (aa) the alien cannot obtain necessary treatment in the foreign state in which the alien is residing; or (bb) the medical emergency is life-threatening and there is insufficient time for the alien to be admitted through the normal visa process; (ii) the alien is the parent or legal guardian of an alien described in clause (i) and the alien described in clause (i) is a minor; (iii) the alien is needed in the United States in order to donate an organ or other tissue for transplant and there is insufficient time for the alien to be admitted through the normal visa process; (iv) the alien has a close family member in the United States whose death is imminent and the alien could not arrive in the United States in time to see such family member alive if the alien were to be admitted through the normal visa process; (v) the alien is seeking to attend the funeral of a close family member and the alien could not arrive in the United States in time to attend such funeral if the alien were to be admitted through the normal visa process; (vi) the alien is an adopted child with an urgent medical condition who is in the legal custody of the petitioner for a final adoption-related visa and whose medical treatment is required before the expected award of a final adoption-related visa; or (vii) the alien is a lawful applicant for adjustment of status under section 245 and is returning to the United States after temporary travel abroad. (E) For purposes of determining an alien's eligibility for parole under subparagraph (A), a significant public benefit may be determined to result from the parole of an alien only if\u2014 (i) the alien has assisted (or will assist, whether knowingly or not) the United States Government in a law enforcement matter; (ii) the alien\u2019s presence is required by the Government in furtherance of such law enforcement matter; and (iii) the alien is inadmissible, does not satisfy the eligibility requirements for admission as a nonimmigrant, or there is insufficient time for the alien to be admitted through the normal visa process. (F) For purposes of determining an alien's eligibility for parole under subparagraph (A), the term case-by-case basis means that the facts in each individual case are considered and parole is not granted based on membership in a defined class of aliens to be granted parole. The fact that aliens are considered for or granted parole one-by-one and not as a group is not sufficient to establish that the parole decision is made on a case-by-case basis . (G) The Secretary of Homeland Security may not use the parole authority under this paragraph to parole an alien into the United States for any reason or purpose other than those described in subparagraphs (B), (C), (D), and (E). (H) An alien granted parole may not accept employment, except that an alien granted parole pursuant to subparagraph (B) or (C) is authorized to accept employment for the duration of the parole, as evidenced by an employment authorization document issued by the Secretary of Homeland Security. (I) Parole granted after a departure from the United States shall not be regarded as an admission of the alien. An alien granted parole, whether as an initial grant of parole or parole upon reentry into the United States, is not eligible to adjust status to lawful permanent residence or for any other immigration benefit if the immigration status the alien had at the time of departure did not authorize the alien to adjust status or to be eligible for such benefit. (J) (i) Except as provided in clauses (ii) and (iii), parole shall be granted to an alien under this paragraph for the shorter of\u2014 (I) a period of sufficient length to accomplish the activity described in subparagraph (D) or (E) for which the alien was granted parole; or (II) 1 year. (ii) Grants of parole pursuant to subparagraph (A) may be extended once, in the discretion of the Secretary, for an additional period that is the shorter of\u2014 (I) the period that is necessary to accomplish the activity described in subparagraph (D) or (E) for which the alien was granted parole; or (II) 1 year. (iii) Aliens who have a pending application to adjust status to permanent residence under section 245 may request extensions of parole under this paragraph, in 1-year increments, until the application for adjustment has been adjudicated. Such parole shall terminate immediately upon the denial of such adjustment application. (K) Not later than 90 days after the last day of each fiscal year, the Secretary of Homeland Security shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives and make available to the public, a report\u2014 (i) identifying the total number of aliens paroled into the United States under this paragraph during the previous fiscal year; and (ii) containing information and data regarding all aliens paroled during such fiscal year, including\u2014 (I) the duration of parole; (II) the type of parole; and (III) the current status of the aliens so paroled. .\n#### 3. Implementation\n##### (a) In general\nExcept as provided in subsection (b), this Act and the amendments made by this Act shall take effect on the date that is 30 days after the date of the enactment of this Act.\n##### (b) Exceptions\nNotwithstanding subsection (a)\u2014\n**(1)**\nany application for parole or advance parole filed by an alien before the date of the enactment of this Act shall be adjudicated under the law that was in effect on the date on which the application was properly filed and any approved advance parole shall remain valid under the law that was in effect on the date on which the advance parole was approved;\n**(2)**\nsection 212(d)(5)(I) of the Immigration and Nationality Act, as added by section 2, shall take effect on the date of the enactment of this Act; and\n**(3)**\naliens who were paroled into the United States pursuant to section 212(d)(5)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1182(d)(5)(A) ) before January 1, 2023, shall continue to be subject to the terms of parole that were in effect on the date on which their respective parole was approved.\n#### 4. Cause of action\nAny person, State, or local government that experiences financial harm in excess of $1,000 due to a failure of the Federal Government to lawfully apply the provisions of this Act or the amendments made by this Act shall have standing to bring a civil action against the Federal Government in an appropriate district court of the United States.\n#### 5. Severability\nIf any provision of this Act or any amendment by this Act, or the application of such provision or amendment to any person or circumstance, is held to be unconstitutional, the remainder of this Act and the application of such provision or amendment to any other person or circumstance shall not be affected.",
      "versionDate": "2025-05-05",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the Subcommittee on Border Security and Enforcement."
      },
      "number": "696",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Unaccountable Amnesty Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "225",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "End Unaccountable Amnesty Act",
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
        "name": "Immigration",
        "updateDate": "2025-05-22T18:10:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-05",
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
          "measure-id": "id119s1589",
          "measure-number": "1589",
          "measure-type": "s",
          "orig-publish-date": "2025-05-05",
          "originChamber": "SENATE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1589v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-05-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Immigration Parole Reform Act of 2025</strong></p><p>This bill limits the authority of the Department of Homeland Security (DHS) to grant immigration parole (i.e., give official permission for an individual to enter and temporarily remain in the United States).</p><p>Specifically, the bill (1) limits what qualifies as an urgent humanitarian reason or a significant public benefit that would justify granting parole, and (2) prohibits granting parole based on an individual's membership in a defined class of individuals.</p><p>An urgent humanitarian reason is limited to medical emergencies, the death of a close family member, and to green card applicants returning to the United States after temporary travel abroad. A significant public benefit is limited to assisting the U.S. government in a law enforcement matter.</p><p>Individuals granted parole on the basis of an urgent humanitarian reason or a significant public benefit are not permitted to work while in the United States.</p><p>Additionally, the bill provides statutory authority for DHS to grant parole to certain Cuban nationals and to certain family members of active-duty Armed Forces members.\u00a0\u00a0</p>"
        },
        "title": "Immigration Parole Reform Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1589.xml",
    "summary": {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Immigration Parole Reform Act of 2025</strong></p><p>This bill limits the authority of the Department of Homeland Security (DHS) to grant immigration parole (i.e., give official permission for an individual to enter and temporarily remain in the United States).</p><p>Specifically, the bill (1) limits what qualifies as an urgent humanitarian reason or a significant public benefit that would justify granting parole, and (2) prohibits granting parole based on an individual's membership in a defined class of individuals.</p><p>An urgent humanitarian reason is limited to medical emergencies, the death of a close family member, and to green card applicants returning to the United States after temporary travel abroad. A significant public benefit is limited to assisting the U.S. government in a law enforcement matter.</p><p>Individuals granted parole on the basis of an urgent humanitarian reason or a significant public benefit are not permitted to work while in the United States.</p><p>Additionally, the bill provides statutory authority for DHS to grant parole to certain Cuban nationals and to certain family members of active-duty Armed Forces members.\u00a0\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1589"
    },
    "title": "Immigration Parole Reform Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Immigration Parole Reform Act of 2025</strong></p><p>This bill limits the authority of the Department of Homeland Security (DHS) to grant immigration parole (i.e., give official permission for an individual to enter and temporarily remain in the United States).</p><p>Specifically, the bill (1) limits what qualifies as an urgent humanitarian reason or a significant public benefit that would justify granting parole, and (2) prohibits granting parole based on an individual's membership in a defined class of individuals.</p><p>An urgent humanitarian reason is limited to medical emergencies, the death of a close family member, and to green card applicants returning to the United States after temporary travel abroad. A significant public benefit is limited to assisting the U.S. government in a law enforcement matter.</p><p>Individuals granted parole on the basis of an urgent humanitarian reason or a significant public benefit are not permitted to work while in the United States.</p><p>Additionally, the bill provides statutory authority for DHS to grant parole to certain Cuban nationals and to certain family members of active-duty Armed Forces members.\u00a0\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1589"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1589is.xml"
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
      "title": "Immigration Parole Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Immigration Parole Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 212(d)(5) of the Immigration and Nationality Act to reform immigration parole, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:24Z"
    }
  ]
}
```
